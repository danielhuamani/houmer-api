from marshmallow import fields, Schema, validates, ValidationError
from .constants import OPEN, EXIT


class CoordinatesValidateSchema(Schema):
    longitude = fields.Float(required=True)
    latitude = fields.Float(required=True)
