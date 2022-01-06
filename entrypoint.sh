#!/bin/bash

set -e  # Configure shell so that if one command fails, it exits

python manage.py migrate
flake8
python manage.py runserver 0.0.0.0:8000
