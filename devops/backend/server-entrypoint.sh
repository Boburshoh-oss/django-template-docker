#!/bin/sh

echo 'Waiting for postgres...'

while ! nc -z $DB_HOSTNAME 5432; do
    sleep 0.1
done

echo 'PostgreSQL started'

echo 'Running migrations...'
cd backend  # <-- Katalogni o'zgartirish
python manage.py migrate

echo 'Collecting static files...'
python manage.py collectstatic --no-input


echo 'Running server...'
gunicorn config.wsgi:application --bind 0.0.0.0:8000
