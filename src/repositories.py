from src.db.models import HoumerModel
from datetime import datetime
from src.utils import now_date

class HoumerRepository:

    def __init__(self):
        self.model = HoumerModel

    def get_last_by_houmer(self, houmer_id):
        houmer = None
        now = now_date().date
        for x in self.model.query(houmer_id, limit=1, scan_index_forward=False):
            houmer = x
        return houmer

    def get_by_range_date(self, houmer_id: int, date_start: datetime, date_end: datetime):
        houmers = self.model.query(
            houmer_id, self.model.date_start.between(date_start, date_end), scan_index_forward=False)
        return houmers

    def get_by_range_date_with_speed(
        self, houmer_id: int, date_start: datetime, date_end: datetime, speed: int):
        houmers = self.model.query(
            houmer_id, 
            self.model.date_start.between(date_start, date_end),
            self.model.speed >= int(speed),
            scan_index_forward=False
        )
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
    