from flask import Flask, request, jsonify
from typing import Any
from flask_server.models.number_model import NumberModel

app = Flask(__name__)
model = NumberModel()


@app.route('/add_number', methods=['POST'])
def add_number() -> Any:
    number = request.json['number']
    model.add_number(number)
    return jsonify(success=True)


@app.route('/get_number/<int:number>', methods=['GET'])
def get_number(number: int) -> Any:
    value = model.get_value(number)
    if value is not None:
        return jsonify(number=number, value=value)
    else:
        return jsonify(error="Number not found"), 404


@app.route('/get_all', methods=['GET'])
def get_all() -> Any:
    return jsonify(model.get_all())
