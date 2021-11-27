from marshmallow import fields, Schema, validates, ValidationError
from .constants import OPEN, EXIT


class CoordinatesValidateSchema(Schema):
    longitude = fields.Float(required=True)
    latitude = fields.Float(required=True)
    houmer_id = fields.Integer(required=True)
    # type_ticket = fields.String(required=True)

    # @validates("type_ticket")
    # def validate_quantity(self, value):
    #     if value in [OPEN, EXIT]:
    #         raise ValidationError("choose option open or exit")