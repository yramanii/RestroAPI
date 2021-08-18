FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /restro

ADD . /restro

COPY ./requirements.txt /restro/requirements.txt

RUN pip install -r requirements.txt

COPY . /restro/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]