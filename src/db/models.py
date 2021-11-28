import os
from datetime import datetime
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute, NumberAttribute, UnicodeAttribute
from .connection import Connection


class HoumerModel(Model):
    
    class Meta:
        region = os.environ.get('REGION', 'us-east-2')
        table_name = os.environ.get('TABLE_HOUMER')
        if Connection.has_host():
            host = Connection.get_host_local()

    id = UnicodeAttribute(hash_key=True)
    houmer_id = NumberAttribute()
    date_start = UTCDateTimeAttribute(null=False, default=datetime.now())
    latitude_start = NumberAttribute()
    longitude_start = NumberAttribute()
    latitude_end = NumberAttribute(null=True)
    longitude_end = NumberAttribute(null=True)
    date_end = UTCDateTimeAttribute(null=True)
    speed = NumberAttribute(null=True)
    distance = NumberAttribute(null=True)
    spend_time = UnicodeAttribute(null=True)