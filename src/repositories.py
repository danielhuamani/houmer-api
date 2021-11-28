from .db.models import HoumerModel
from datetime import datetime

class HoumerRepository:

    def __init__(self):
        self.model = HoumerModel

    def get_last_by_houmer(self, id):
        houmer = None
        for x in self.model.scan(self.model.houmer_id==id, limit=1):
            houmer = x
        return houmer

    def get_by_range_date(self, houmer_id: int, date_start: datetime, date_end: datetime):
        houmers = self.model.scan((self.model.houmer_id == houmer_id) & (self.model.date_start >= date_start) & (self.model.date_start < date_end))
        return houmers

    def get_by_range_date_with_speed(
        self, houmer_id: int, date_start: datetime, date_end: datetime, speed: int):
        houmers = self.model.scan((self.model.houmer_id == houmer_id) & (self.model.date_start >= date_start) & (self.model.date_start < date_end) & (self.model.speed >= int(speed)))
        return houmers

    def update(self, instance, data):
        for attr, value in data.items():
            setattr(instance, attr, value)
            setattr(instance, attr, value)
        instance.save()
        return instance
    
    def create(self, data):
        instance = HoumerModel()
        for attr, value in data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    