from flask import Flask, request, jsonify
from geopy import distance
from marshmallow import ValidationError
from .models import HoumerModel
from .validations import CoordinatesValidateSchema
from datetime import date, datetime, timezone, timedelta
from time import strftime, gmtime
from geopy.distance import geodesic as GD  
from uuid import uuid4
app = Flask(__name__)


@app.route("/houmer/coordinates", methods=['POST'])
def coordinates():
    request_data = request.get_json()
    try:
        result = CoordinatesValidateSchema().load(request_data)
        now_date = datetime.now(timezone.utc)
        print(now_date)
        last_houmer = HoumerModel.scan(HoumerModel.date_start==now_date, rate_limit=1)
        # ho = HoumerModel(houmer_id=result.get("houmer_id"), latitude_start=result.get("latitude"), longitude_start=result.get("longitude"), id=str(uuid4()))
        # ho.save()
        # print(ho.id, "id")
        print('last_houmer', HoumerModel.count())
        houmer = None
        for item in HoumerModel.scan(HoumerModel.houmer_id==2, limit=1):
            print("Query returned item {0}".format(item), item.date_start, item.date_start.date())
            houmer = item
        print(houmer)
        if houmer:
            latitude_start = houmer.latitude_start
            longitude_start = houmer.longitude_start
            latitude_end = result.get('latitude')
            longitude_end = result.get('longitude')
            point_start = (latitude_start, longitude_start)
            point_final = (latitude_end, longitude_end)
            distance = (GD(point_start, point_final).km)
            distance_mt2 = distance * 1000
            if distance_mt2 > 100:
                spend_time = now_date - houmer.date_start
                spend_time_hour = spend_time.seconds / 3600
                houmer.latitude_end = latitude_end
                houmer.longitude_end = longitude_end
                houmer.distance = distance
                houmer.date_end = now_date
                houmer.spend_time = strftime("%H:%M", gmtime(spend_time.seconds))
                houmer.speed = distance / spend_time_hour
                houmer.save()
            print(point_final, point_start, latitude_start, longitude_start)
            print(GD(point_start, point_final).km, "dasdsdsads")
        else:
            ho = HoumerModel(houmer_id=result.get("houmer_id"), latitude_start=result.get("latitude"), longitude_start=result.get("longitude"), id=str(uuid4()))
            ho.save()
    except ValidationError as err:
        print(err.messages)
    print(HoumerModel.count(), request_data, type(request_data))
    return "Hello World!"


@app.route("/houmer/<id>/<selected_date>/visit", methods=['GET'])
def visit(id, selected_date):
    houmer_id = id
    selected_date = datetime.strptime(selected_date, "%Y-%m-%d")
    selected_date_start = selected_date.replace(tzinfo=timezone.utc, hour=0, minute=0, second=0, microsecond=0)
    selected_date_end = selected_date + timedelta(hours=24)
    items = HoumerModel.scan((HoumerModel.houmer_id == int(houmer_id)) & (HoumerModel.date_start >= selected_date) & (HoumerModel.date_start < selected_date_end))
    items_serializer = []
    for x in items:
    
        items_serializer.append({
            "latitude": x.latitude_start,
            "longitude": x.longitude_start,
            "spend_time": x.spend_time,
            "date": {
                "start": x.date_start.strftime("%Y-%m-%d %H:%M"),
                "end": x.date_end.strftime("%Y-%m-%d %H:%M") if x.date_end else None
            }
        })
    print(items_serializer)
    return jsonify(items_serializer), 200


@app.route("/houmer/<id>/<selected_date>/speed/<speed>", methods=['GET'])
def speed(id, selected_date, speed):
    houmer_id = id
    selected_date = datetime.strptime(selected_date, "%Y-%m-%d")
    selected_date_start = selected_date.replace(tzinfo=timezone.utc, hour=0, minute=0, second=0, microsecond=0)
    selected_date_end = selected_date + timedelta(hours=24)
    items = HoumerModel.scan((HoumerModel.houmer_id == int(houmer_id)) & (HoumerModel.date_start >= selected_date) & (HoumerModel.date_start < selected_date_end) & (HoumerModel.speed >= int(speed)))
    items_serializer = []
    for x in items:
        items_serializer.append({
            "latitude": x.latitude_start,
            "longitude": x.longitude_start,
            "speed": x.speed,
            "date": {
                "start": x.date_start.strftime("%Y-%m-%d %H:%M"),
                "end": x.date_end.strftime("%Y-%m-%d %H:%M") if x.date_end else None
            }
        })
    print(items_serializer)
    return jsonify(items_serializer), 200