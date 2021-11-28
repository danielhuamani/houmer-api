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
                "latitude": houmer.latitude_start,
                "longitude": houmer.longitude_start,
                "spend_time": houmer.spend_time,
                "date": {
                    "start": houmer.date_start.strftime("%Y-%m-%d %H:%M"),
                    "end": houmer.date_end.strftime("%Y-%m-%d %H:%M") if houmer.date_end else None
                }
            })
        return data
    
    def speed(self, houmers):
        data = []
        for houmer in houmers:
            data.append({
                "latitude": houmer.latitude_start,
                "longitude": houmer.longitude_start,
                "speed": houmer.speed,
                "date": {
                    "start": houmer.date_start.strftime("%Y-%m-%d %H:%M"),
                    "end": houmer.date_end.strftime("%Y-%m-%d %H:%M") if houmer.date_end else None
                }
            })
        return data