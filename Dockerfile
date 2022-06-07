# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

# RUN apt-get install libgomp1

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "app.py", "--config_path", "configs/default.json"]
