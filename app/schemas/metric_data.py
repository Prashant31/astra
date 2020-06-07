from .. import ma
from ..models.metric_data import MetricData


class MetricDataSchema(ma.ModelSchema):

    class Meta:
        model = MetricData


metric_data_schema = MetricDataSchema()
metric_datum_schema = MetricDataSchema(many=True)
