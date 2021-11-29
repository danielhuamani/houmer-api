import os
from src.repositories import HoumerRepository
from src.db.models import HoumerModel
from src.exceptions import InvalidMaxDistanceVisit
from src.utils import (now_date, seconds_to_str, date_to_datetime, range_datetime, convert_seconds_to_hours, convert_km_to_mt2)
from datetime import timezone, timedelta, date
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
        return distance

    def complete_visit(self, latitude, longitude, houmer):
        latitude_start = houmer.latitude_start
        longitude_start = houmer.longitude_start
        latitude_end = latitude
        longitude_end = longitude
        point_start = (latitude_start, longitude_start)
        point_end = (latitude_end, longitude_end)
        distance = self.calculate_distance_km(point_start, point_end)
        distance_mt2 = convert_km_to_mt2(distance)
        if distance_mt2 < self.MT2_MAX:
            print(now_date(), houmer.date_start, "*" * 20)
            spend_time = now_date() - houmer.date_start
            data = {
                "date_end": now_date(),
                "spend_time": seconds_to_str(spend_time.seconds),
            }
            return self.repository.update(houmer, data)
        else:
            raise InvalidMaxDistanceVisit("maximum distance not allowed")

    def create_or_update(self, houmer_id, latitude, longitude):
        houmer = self.repository.get_last_by_houmer(houmer_id)
        if houmer.latitude_end is None and houmer.longitude_end is None and houmer.date_end is not None:
            point_start = (houmer.latitude_start, houmer.longitude_start)
            point_end = (latitude, longitude)
            distance = self.calculate_distance_km(point_start, point_end)
            spend_time = now_date() - houmer.date_end.replace(tzinfo=None)
            spend_time_hour = convert_seconds_to_hours(spend_time.seconds)
            if spend_time_hour == float(0):
                speed = 0
            else:
                speed = distance / spend_time_hour
            data = {
                "speed": speed,
                "distance": distance,
                "latitude_end": latitude,
                "longitude_end": longitude,
                "date_enter_next_property": now_date()
            }
            self.repository.update(houmer, data)
        data = {
            "houmer_id": houmer_id,
            "latitude_start": latitude,
            "longitude_start": longitude,
            "id": self.generate_id()
        }
        return self.repository.create(data)

    def create(self, **data: dict):
        data = {**data, "id": self.generate_id()}
        return self.repository.create(data)
    
    def get_by_date(self, houmer_id: int, selected_date: date):
        date_start = date_to_datetime(selected_date)
        date_start = date_start.replace(tzinfo=timezone.utc, hour=0, minute=0, second=0, microsecond=0)
        date_end = date_start + timedelta(hours=24)
        return self.repository.get_by_range_date(houmer_id, date_start, date_end)
    
    def get_by_date_with_speed(self, houmer_id: int, selected_date: date, speed: int):
        date_start = date_to_datetime(selected_date)
        date_start, date_end = range_datetime(date_start)
        return self.repository.get_by_range_date_with_speed(houmer_id, date_start, date_end, speed)
    
    def generate_id(self):
        return str(uuid4())