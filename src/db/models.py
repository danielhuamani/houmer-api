import os
from datetime import datetime
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute, NumberAttribute, UnicodeAttribute
from src.db.connection import Connection


class HoumerModel(Model):
    
    class Meta:
        region = os.environ.get('REGION', 'us-east-2')
        table_name = os.environ.get('TABLE_HOUMER')
        if Connection.has_host():
            host = Connection.get_host_local()

    id = UnicodeAttribute()
    houmer_id = NumberAttribute(hash_key=True)
    date_start = UTCDateTimeAttribute(null=False, default=datetime.now(), range_key=True)
    latitude_start = NumberAttribute()
    longitude_start = NumberAttribute()
    date_end = UTCDateTimeAttribute(null=True)
    speed = NumberAttribute(null=True)
    distance = NumberAttribute(null=True)
    spend_time = UnicodeAttribute(null=True)
    date_enter_next_property = UTCDateTimeAttribute(null=True)
    latitude_end = NumberAttribute(null=True)
    longitude_end = NumberAttribute(null=True)