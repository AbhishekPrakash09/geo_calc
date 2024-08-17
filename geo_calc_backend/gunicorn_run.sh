#!/bin/sh

gunicorn --bind 0.0.0.0:8000 -w 4 geo_calc_backend.wsgi:application