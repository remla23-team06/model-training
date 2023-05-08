FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/
COPY /data /app/
COPY trained_model /app/

RUN pip install -r requirements.txt

EXPOSE 8089