from .. import db
import app
import base64, hashlib, random
from passlib.apps import custom_app_context as api_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
import uuid


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True, nullable=False)
    api_key_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return 'Account {}>'.format(self.name)

    def hash_api_key(self):
        new_key = self.__generate_key()
        self.api_key_hash = api_context.encrypt(new_key)

    def generate_auth_token(self, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id, "name": self.name})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
            return data
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token

    @staticmethod
    def __generate_key():
        return uuid.uuid4().hex
