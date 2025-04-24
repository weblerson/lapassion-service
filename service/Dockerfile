FROM python:3.12

RUN apt-get update

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY ./ ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
