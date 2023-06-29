FROM python:3.10

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=1.5.0
    ENV PATH="$PATH:$POETRY_HOME/bin"

WORKDIR /app

# Copy the pyproject and lock file into app
COPY . /app

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set the environment to use
RUN poetry env use 3.10

# Install dependencies
RUN poetry config installer.max-workers 10
RUN poetry update -vv

# Run DVC repro first
RUN poetry run dvc repro

ENTRYPOINT /bin/bash

EXPOSE 8089