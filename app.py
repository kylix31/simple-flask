from typing import Any

from flask import Flask

from flask_server.controller.number_controller import NumberController

app = Flask(__name__)

controller = NumberController()


@app.route('/add_number', methods=['POST'])
def add_number() -> Any:
    return controller.add_number()


@app.route('/get_number/<int:number>', methods=['GET'])
def get_number(number: int) -> Any:
    return controller.get_number(number)


@app.route('/get_all', methods=['GET'])
def get_all() -> Any:
    return controller.get_all()
