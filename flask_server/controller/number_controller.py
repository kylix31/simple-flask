from typing import Any
from flask import jsonify, request
from flask_server.models.number_model import NumberModel

model = NumberModel()


class NumberController:

    def add_number(self) -> Any:
        """
        Adds a number to the NumberModel.

        Returns:
            A JSON response indicating success or failure.

        Raises:
            ValueError: If the input is not a valid integer.
        """
        number = request.json['number']

        if not isinstance(number, int):
            return jsonify(error='The input is not a valid integer.'), 400

        model.add_number(number)
        return jsonify(success=True)

    def get_number(self, number: int) -> Any:
        """
        Retrieves the value associated with a given number from the NumberModel.

        Args:
            number: The number to retrieve the value for.

        Returns:
            A JSON response containing the number and its associated value.

        Raises:
            KeyError: If the number is not found in the NumberModel.
        """
        value = model.get_value(number)
        if value is not None:
            return jsonify(number=number, value=value)

        return jsonify(error="Number not found"), 404

    def get_all(self) -> Any:
        """
        Retrieves all numbers and their associated values from the NumberModel.

        Returns:
            A JSON response containing all numbers and their associated values.
        """
        return jsonify(model.get_all())
