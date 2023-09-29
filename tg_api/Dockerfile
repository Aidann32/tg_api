FROM python:3.9.2

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip

COPY ./req.txt /usr/src/app/

RUN pip install -r req.txt

COPY ./usr/src/app/