# 'Students database' web application

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Overview

It allows you to track attendance of your students. Manage exams, add or edit students, groups, etc.

## Technical Stack

- Python 3.5.2
- Django 1.11.1
- Django REST Framework 3.6.2 
- PostgreSQL(Docker)
- Twitter Bootstrap
- jQuery

## Installation

### Clone project

```sh
$ virtualenv -p python3.5 venv
$ . venv/bin/activate
(venv)$ git clone https://github.com/val-sytch/studentsdb.git
```

### Install requirements

```sh
(venv)$ pip install -r requirements/base.txt
```

### Database

You can setup your own DB(install PostgreSQL server on your local machine, create DB and set custom settings 
in settings.py) or use dockerized PostgreSQL (-p 5434, -U students_db_user, -d students_db, -p 435363)
from <docker-compose.yml> - All credentials there.

To use Docker you need firstly install 'docker engine' and 'docker-compose'.
https://docs.docker.com/compose/install/

Run docker:
```sh
$ sudo service docker start
```

Then, from project root run(build and run container):
```sh
$ sudo docker-compose up -d
```

List of containers:
```sh
$ sudo docker-compose ps
```

### Run application

```sh
(venv)$ python manage.py migrate
(venv)$ python manage.py loaddata demo_data.json
(venv)$ python manage.py createsuperuser
(venv)$ python manage.py runserver
```

## Run tests

```sh
(venv)$ python manage.py test
```

### Check code coverage
```sh
(venv)$ pip install -r requirements/test.txt
(venv)$ coverage run --omit='venv/*' manage.py test
(venv)$ coverage report
```