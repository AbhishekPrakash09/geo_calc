#!/bin/sh

echo "Running Django migrations..."
python manage.py migrate

echo "Starting geo_calc application..."
gunicorn --bind 0.0.0.0:8000 -w 4 geo_calc_backend.wsgi:application