from flask import request, abort, g
from functools import wraps
from ..models.account import Account
from app import cache


def validate_license(api_method):
    @wraps(api_method)
    def check_license(*args, **kwargs):
        license_key = request.headers.get('X-License-Key')
        if license_key is None:
            return abort(401)
        request_account_id = cache.get(license_key)
        if request_account_id is None:
            request_account = Account.query.filter_by(api_key=license_key).first()
            if request_account is not None:
                cache.set(license_key, request_account.id)
                request_account_id = request_account.id
            else:
                abort(401)
        g.account_id = request_account_id
        return api_method(*args, **kwargs)
    return check_license
