from flask import Flask, request
from .models import HoumerModel

app = Flask(__name__)


@app.route("/coordinates", methods=['POST'])
def coordinates():
    request_data = request.get_json()
    print(HoumerModel.count(), request_data, type(request_data))
    return "Hello World!"
