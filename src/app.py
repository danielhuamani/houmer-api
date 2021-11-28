from flask import Flask, request, jsonify
from geopy import distance
from marshmallow import ValidationError
from .services import HoumerService
from .db.models import HoumerModel
from .validations import CoordinatesValidateSchema
from .utils import now_date
from .exceptions import InvalidMaxDistanceVisit
from datetime import date, datetime, timezone, timedelta
from time import strftime, gmtime
from geopy.distance import geodesic as GD  
app = Flask(__name__)


@app.route("/houmer/<houmer_id>/coordinates", methods=['POST'])
def coordinates(houmer_id):
    request_data = request.get_json()
    service = HoumerService()
    try:
        result = CoordinatesValidateSchema().load(request_data)
        houmer_id = int(houmer_id)
        houmer = service.get_last_by_houmer(houmer_id=houmer_id)
        if houmer is not None:
            latitude = result.get('latitude')
            longitude = result.get('longitude')
            try:
                instance = service.complete_visit(latitude, longitude, houmer)
            except InvalidMaxDistanceVisit as err:
                instance = service.create(houmer_id=result.get("houmer_id"), latitude_start=result.get("latitude"), longitude_start=result.get("longitude"))
        else:
            print(houmer_id, "houmer_id")
            instance = service.create(houmer_id=houmer_id, latitude_start=result.get("latitude"), longitude_start=result.get("longitude"))
        return jsonify({
            "latitude": instance.latitude_start,
            "longitude": instance.longitude_start,
            "houmer_id": instance.houmer_id,
            "id": instance.id
        }), 201
    except ValidationError as err:
        return jsonify(err), 403


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