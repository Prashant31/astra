from .. import db


class MetricData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False, index=True)
    timestamp = db.Column(db.BigInteger, nullable=False)
    metric_name = db.Column(db.String(32), nullable=False)
    metric_value = db.Column(db.Float)
