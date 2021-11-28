from .db.models import HoumerModel


class HoumerRepository:

    def get_last_by_houmer(self, id):
        houmer = None
        for x in HoumerModel.scan(HoumerModel.houmer_id==id, limit=1):
            houmer = x
        return houmer

    def update(self, instance, data):
        print(instance.latitude_start)
        for attr, value in data.items():
            print(attr, value)
            setattr(instance, attr, value)
            setattr(instance, attr, value)
        instance.save()
        print(instance.latitude_start)
        # instance.refresh()
        return instance
    
    def create(self, data):
        instance = HoumerModel()
        for attr, value in data.items():
            print(attr, value)
            setattr(instance, attr, value)
        print(instance.houmer_id, instance.id)
        instance.save()
        return instance
    