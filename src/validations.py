from marshmallow import fields, Schema
from werkzeug.routing import BaseConverter, ValidationError
from datetime import datetime, date


class CoordinatesValidateSchema(Schema):
    longitude = fields.Float(required=True)
    latitude = fields.Float(required=True)


class ISODateConverter(BaseConverter):

    regex = r'\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        try:
            # try and convert a string to a datetime object and then get a date object
            return datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError:
            raise ValidationError()

    def to_url(self, value):
        if isinstance(value, date):
            return value.strftime('%Y-%m-%d')