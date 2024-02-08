# :rocket: simple-flask

## Introduction

Welcome to the Flask Number Server, a sophisticated REST API designed for number operations and type identification, implemented conforming to the MVC (Model-View-Controller) architectural pattern and SOLID design principles.

Built with PRODUCTION-READINESS in mind and leveraging modern software architecture standards, this server is not only about executing operations but also illustrating best practices in Python and Flask application development.

## Getting Started

```bash
git clone https://github.com/your-username/flask-number-server.git
cd simple-flask
poetry install
```

### Using Docker

Streamline your deployment using the encapsulated Docker environment:

```bash
docker-compose up --build
```

*Note*: Ensure you have Docker and Docker Compose installed.

## Features

The Flask Number Server allows you to:

- Add numbers with adherence to custom type rules using a POST request.
- Retrieve a single number's type, if present, using a GET request.
- Fetch all numbers and their associated types via a GET request.

## Usage

### Add a Number

```curl
curl -X POST http://localhost:5000/add_number -H 'Content-Type: application/json' -d '{"number": 15}'
```

### Get a Number's Type

```curl
curl http://localhost:5000/get_number/15
```

### Get All Numbers

```curl
curl http://localhost:5000/get_all
```

## Project Structure

The server is structured based on the MVC design pattern:

- `app.py`: The entry point of the application that defines the routes.
- `controller/number_controller.py`: Houses the business logic as the Controller.
- `services/number_printer.py`: The Service layer, applying Number type determination logic.
- `models/number_model.py`: Represents data and business logic in the Model layer.
- `core/contracts/*`: Defines interfaces and types keeping in line with SOLID's "Dependency Inversion Principle."

Implemented **SOLID** techniques ensure:

- Single Responsibility (clearly separated logic)
- Open-Closed (extensible codebase)
- Liskov Substitution (interchangeable components)
- Interface Segregation (targeted, lean interfaces)
- Dependency Inversion (decoupled code)

## Testing

To perform the available unit tests, just do:

```bash
poetry run python -m unittest tests.test_server
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
