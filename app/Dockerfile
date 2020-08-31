FROM python:3.6-slim

RUN pip install flask

WORKDIR /app

EXPOSE 8000

COPY ./ ./

ENV FLASK_APP=./main.py

CMD flask run --host=0.0.0.0 --port=8000
