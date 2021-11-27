from marshmallow import fields, Schema, validates, ValidationError
from .constants import OPEN, EXIT


class VisitSerializerSchema(Schema):
    latitude = fields.Float()
    longitude = fields.Float()
    spend_time = fields.String()
