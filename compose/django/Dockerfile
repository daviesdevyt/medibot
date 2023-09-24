FROM python:3.11.4-slim-bullseye

ENV PYTHONUNBUFFERED 1

RUN sudo apt-get update && sudo apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev

RUN sudo apt-get install gunicorn

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
