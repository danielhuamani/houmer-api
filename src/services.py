import os
from .repositories import HoumerRepository
from .exceptions import InvalidMaxDistanceVisit
from .utils import now_date, seconds_to_str
from datetime import date, datetime, timezone, timedelta
from time import strftime, gmtime
from geopy.distance import geodesic as GD
from uuid import uuid4


class HoumerService:

    def __init__(self):
        self.repository = HoumerRepository()
        self.MT2_MAX = float(os.environ.get('MT2_MAX', 150))


    def get_last_by_houmer(self, houmer_id: int):
        return self.repository.get_last_by_houmer(houmer_id)
    
    def calculate_distance_km(self, point_start, point_end):
        distance = GD(point_start, point_end).km
        print(type(distance))
        return distance

    def complete_visit(self, latitude, longitude, houmer):
        latitude_start = houmer.latitude_start
        longitude_start = houmer.longitude_start
        latitude_end = latitude
        longitude_end = longitude
        point_start = (latitude_start, longitude_start)
        point_end = (latitude_end, longitude_end)
        distance = self.calculate_distance_km(point_start, point_end)
        distance_mt2 = distance * 1000
        if distance_mt2 < self.MT2_MAX:
            spend_time = now_date() - houmer.date_start
            spend_time_hour = spend_time.seconds / 3600
            houmer.latitude_end = latitude_end
            houmer.longitude_end = longitude_end
            houmer.distance = distance
            houmer.date_end = now_date()
            houmer.spend_time = strftime("%H:%M", gmtime(spend_time.seconds))
            houmer.speed = distance / spend_time_hour
            houmer.save()
            data = {
                "latitude_end": latitude_end,
                "longitude_end": longitude_end,
                "distance": distance,
                "date_end": now_date(),
                "spend_time": seconds_to_str(spend_time.seconds)
            }
            return self.repository.update(houmer, data)
        else:
            raise InvalidMaxDistanceVisit("Distance max not allowed")

    def create(self, **data: dict):
        data = {**data, "id": str(uuid4())}
        return self.repository.create(data)
    
    def get_by_date(self, houmer_id: int, selected_date: str):
        date_start = datetime.strptime(selected_date, "%Y-%m-%d")
        date_start = date_start.replace(tzinfo=timezone.utc, hour=0, minute=0, second=0, microsecond=0)
        date_end = date_start + timedelta(hours=24)
        return self.repository.get_by_range_date(houmer_id, date_start, date_end)
    
    def get_by_date_with_speed(self, houmer_id: int, selected_date: str, speed: int):
        date_start = datetime.strptime(selected_date, "%Y-%m-%d")
        date_start = date_start.replace(tzinfo=timezone.utc, hour=0, minute=0, second=0, microsecond=0)
        date_end = date_start + timedelta(hours=24)
        return self.repository.get_by_range_date_with_speed(houmer_id, date_start, date_end, speed)