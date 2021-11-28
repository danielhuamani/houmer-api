from flask import Flask, request, jsonify
from geopy import distance
from marshmallow import ValidationError
from .services import HoumerService
from .db.models import HoumerModel
from .validations import CoordinatesValidateSchema
from .utils import now_date
from .exceptions import InvalidMaxDistanceVisit
from .serializers import HoumerSerializer
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
            instance = service.create(houmer_id=houmer_id, latitude_start=result.get("latitude"), longitude_start=result.get("longitude"))
        serializer = HoumerSerializer()
        return jsonify(serializer.coordinates(instance)), 201
    except ValidationError as err:
        return jsonify(err), 403


@app.route("/houmer/<id>/<selected_date>/visit", methods=['GET'])
def visit(id, selected_date):
    houmer_id = int(id)
    service = HoumerService()
    houmers = service.get_by_date(houmer_id=houmer_id, selected_date=selected_date)
    serializer = HoumerSerializer()
    return jsonify(serializer.visit(houmers)), 200


@app.route("/houmer/<id>/<selected_date>/speed", methods=['GET'])
def speed(id, selected_date):
    houmer_id = int(id)
    speed = request.args.get('speed', 0, type=int)
    service = HoumerService()
    houmers = service.get_by_date_with_speed(
        houmer_id=houmer_id, selected_date=selected_date, speed=speed)
    serializer = HoumerSerializer()
    return jsonify(serializer.speed(houmers)), 200