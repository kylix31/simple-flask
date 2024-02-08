from typing import Any

from flask import jsonify, request

from flask_server.models.number_model import NumberModel

model = NumberModel()


class NumberController:

    def add_number(self) -> Any:
        number = request.json['number']

        if not isinstance(number, int):
            return jsonify(error='The input is not a valid integer.'), 400

        model.add_number(number)
        return jsonify(success=True)

    def get_number(self, number: int) -> Any:
        value = model.get_value(number)
        if value is not None:
            return jsonify(number=number, value=value)

        return jsonify(error="Number not found"), 404

    def get_all(self) -> Any:
        return jsonify(model.get_all())
