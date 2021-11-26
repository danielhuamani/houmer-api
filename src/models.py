import os
from datetime import datetime
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute, NumberAttribute
from .db.connection import Connection


class HoumerModel(Model):
    
    class Meta:
        region = os.environ.get('REGION', 'us-east-2')
        table_name = os.environ.get('TABLE_HOUMER')
        if Connection.has_host():
            host = Connection.get_host_local()

    id = UnicodeAttribute(hash_key=True)
    date_start = UTCDateTimeAttribute(null=False, default=datetime.now())
    lat_start = NumberAttribute()
    lng_start = NumberAttribute()
    lat_end = NumberAttribute()
    lng_end = NumberAttribute()
    date_end = UTCDateTimeAttribute(null=True)
    speed = NumberAttribute(null=True)
    distance = NumberAttribute(null=True)