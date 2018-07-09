# Django Sites Web

![Travis](https://img.shields.io/travis/LuanP/django_sites_web.svg) ![Coveralls github](https://img.shields.io/coveralls/github/LuanP/django_sites_web.svg) [![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg)](https://github.com/LuanP/django_sites_web)

> A 3MW Application Task.

The task is to develop an application as shown on http://applicationtask.herokuapp.com. The requirements are as follow:

- Django as web framework
- Bootstrap as front-end framework
- Keep the URL logic
- Regarding the aggregations: please implement one in Python code and the other one as database query, using Django's database API over raw SQL.

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [API](#api)
- [Contribute](#contribute)
- [License](#license)


## Background

This project was built and tested with `Python 3.6.4`.

It's recommended that you use docker-compose for running this project.

The project uses `SQLite` as testing database and `Postgres` for develop/stage/production environments.

## Install

Just run:

```
docker-compose up
```

**NOTE:** If you want to develop any feature, make sure to run:

```
make install-development
```

This will set you some git-hooks to run `flake8` and `coverage` before every commit and push.

### Manual install

If you want it, it's recommended to create a [virtualenv](http://virtualenvwrapper.readthedocs.io/en/latest/).

Create your database and user:

```
psql -c "CREATE USER your_user WITH PASSWORD 'your_password';" -U postgres
psql -c "CREATE DATABASE your_db;" -U postgres
psql -c "GRANT ALL PRIVILEGES ON DATABASE your_db TO your_user;" -U postgres
```

Copy the `.env.sample` and set the variables as you wish:

```
cp .env.sample .env
vi .env
```

Install and run the project:
```
make install-development
```

## Usage

If you have chosen the path of happiness using docker-compose you will be set up and running only with the command of the previous section:

```
docker-compose up
```

### Manual usage

```
python3 src/manage.py migrate
python3 src/manage.py loaddata sites  # optional: only if you want some previous data
python3 src/manage.py runserver 0.0.0.0:8000
```

## Contribute

PRs accepted.

Small note: If editing the Readme, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

[GNU General Public License v3.0](./LICENSE)
