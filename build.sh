#!/bin/bash

python manage.py migrate
exec gunicorn -w 3 medibot.wsgi --daemon