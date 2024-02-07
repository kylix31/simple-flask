from models.number_model import NumberModel

model = NumberModel()


def save_number(number):
    value = model.add_number(number)
    return jsonify({"number": number, "value": value}), 201


def get_number_value(number):
    value = model.get_value(number)
    if value is None:
        abort(404, description=f"Number {number} not found.")
    return jsonify({"number": number, "value": value})


def get_all_numbers():
    all_numbers = model.get_all()
    return jsonify(all_numbers)
