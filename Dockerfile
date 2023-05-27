FROM python:3.10

WORKDIR /app

COPY /data /app/
COPY /src /app/
COPY /tests /app/

RUN poetry install
RUN poetry env use 3.10

EXPOSE 8089