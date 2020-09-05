FROM python:3.6

RUN pip install flask
RUN pip install uwsgi

WORKDIR /flask

EXPOSE 8000

COPY ./ ./

CMD ["uwsgi","app.ini"]
#ENV FLASK_APP=./app/main.py

#ENTRYPOINT flask run --host=0.0.0.0 --port=8000
