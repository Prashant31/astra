from .. import db


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True, nullable=False)
    api_key = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return 'Account {}>'.format(self.name)
