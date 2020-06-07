from marshmallow_sqlalchemy import ModelSchema


class AccountSchema(ModelSchema):
    class Meta:
        fields = ('id', 'name')


account_schema = AccountSchema()
