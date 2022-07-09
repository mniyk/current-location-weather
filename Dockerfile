FROM python:3.10-buster

RUN apt update && \
    pip install --upgrade pip