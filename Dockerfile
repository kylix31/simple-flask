# Use the official Python image with a specific version as a parent image
FROM python:3-slim

# Set an environment variable to store where the app is installed to inside of the Docker image
ENV APP_HOME /app
WORKDIR $APP_HOME

# Install Poetry
ENV POETRY_VERSION 1.7.1
RUN pip install "poetry==$POETRY_VERSION"

# Copy the poetry.lock* in case it doesn't exist in the repo and pyproject.toml files
COPY pyproject.toml poetry.lock* $APP_HOME/

# Install runtime dependencies using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-dev

# Copy the rest of the application's code
COPY . $APP_HOME

# Expose the port the app runs on
EXPOSE 5000

# Start the application
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]

