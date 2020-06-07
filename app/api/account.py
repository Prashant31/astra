import uuid

from flask import jsonify, request, abort

from . import api
from .. import db
from ..models.account import Account
from ..schemas.account_schema import account_schema
from .utils import validate_license


@api.route('/accounts/create', methods=['POST'])
def create_account():
    name = request.json.get('name')
    if name is None:
        abort(400)  # missing arguments
    if Account.query.filter_by(name=name).first() is not None:
        abort(400)  # existing account
    api_key = __generate_key()
    account = Account(name=name, api_key=api_key)
    db.session.add(account)
    db.session.commit()
    return jsonify({"account": account_schema.dump(account), "api_key": api_key})


@api.route('/account/<int:account_id>', methods=['GET'])
@validate_license
def account_details(account_id):
    account = Account.query.get(account_id)
    return jsonify(account_schema.dump(account))


def __generate_key():
    return uuid.uuid4().hex
