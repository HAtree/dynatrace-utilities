FROM python:3.5

MAINTAINER Henry Apletree "henry.apletree@dynatrace.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
RUN pwd
COPY . /app

ENTRYPOINT ["python"]

CMD ["app.py"]