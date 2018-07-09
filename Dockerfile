FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

ADD requirements/ /usr/src/app/requirements/

RUN pip install -r requirements/production.txt

ADD . /usr/src/app/

ENTRYPOINT ["./entrypoint.sh"]
