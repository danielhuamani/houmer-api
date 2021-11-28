from marshmallow import fields, Schema


class CoordinatesValidateSchema(Schema):
    longitude = fields.Float(required=True)
    latitude = fields.Float(required=True)
