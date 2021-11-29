from src.utils import calculate_distance_km, convert_seconds_to_hours

class HoumerSerializer:

    def coordinates(self, houmer):
        return {
            "latitude": houmer.latitude_start,
            "longitude": houmer.longitude_start,
            "houmer_id": houmer.houmer_id,
            "id": houmer.id
        }
    
    def visit(self, houmers):
        data = []
        for houmer in houmers:
            data.append({
                "houmer_id": houmer.houmer_id,
                "id": houmer.id,
                "latitude": houmer.latitude_start,
                "longitude": houmer.longitude_start,
                "date_enter_property":  houmer.date_start.strftime("%Y-%m-%d %H:%M:%S"),
                "date_leave_propery": houmer.date_end.strftime("%Y-%m-%d %H:%M:%S") if houmer.date_end else None,
                "spend_time": houmer.spend_time
            })
        return data
    
    def speed(self, houmers):
        data = []
        x = 0
        houmer_prev = None
        for houmer in houmers:
            visits = {
                "leave_property": {
                    "latitude": houmer.latitude_start,
                    "longitude": houmer.longitude_start,
                    "date": houmer.date_end
                },
                "enter_property": {
                    "latitude": houmer.latitude_end,
                    "longitude": houmer.longitude_end,
                    "date": houmer.date_enter_next_property
                },
                "speed": {
                    "value": houmer.speed,
                    "type": "km/h"
                },
                "distance": {
                    "value": houmer.distance,
                    "type": "km"
                }
            }
            data.append(visits)
        return data