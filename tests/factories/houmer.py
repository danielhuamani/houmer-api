from src.db.models import HoumerModel

def create_houmer(
    id, houmer_id, date_start, latitude_start, longitude_start,
    latitude_end=None, longitude_end=None, date_end=None, speed=None, distance=None,
    spend_time=None):
    houmer = HoumerModel()
    houmer.id = id
    houmer.houmer_id = houmer_id
    if date_start:
        houmer.date_start = date_start
    houmer.latitude_start = latitude_start
    houmer.longitude_start = longitude_start
    houmer.latitude_end = latitude_end
    houmer.longitude_end = longitude_end
    houmer.date_end = date_end
    houmer.speed = speed
    houmer.distance = distance
    houmer.spend_time = spend_time
    houmer.save()
    return houmer