FROM python:3.11

WORKDIR app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERE 1

COPY requirements.txt /add

RUN pip install -r requirements.txt

COPY .. /add