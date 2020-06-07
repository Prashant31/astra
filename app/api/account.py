from flask import jsonify, request, abort
from . import api
from .. import db
from ..models.account import Account
from ..schemas.account_schema import account_schema


@api.route('/accounts/create', methods=['POST'])
def create_account():
    name = request.json.get('name')
    if name is None:
        abort(400)  # missing arguments
    if Account.query.filter_by(name=name).first() is not None:
        abort(400)  # existing account

    account = Account(name=name)
    account.hash_api_key()
    db.session.add(account)
    db.session.commit()
    return jsonify(account_schema.dump(account))
