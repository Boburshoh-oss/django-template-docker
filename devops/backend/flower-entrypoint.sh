#!/bin/sh

until cd /code/backend
do
    echo "Waiting for server worker..."
done

until timeout 10 celery -A config inspect ping; do
    >&2 echo "Celery workers not available"
done
echo 'Starting flower'

# run a worker :)
celery -A config flower --port=5555 --persistent=True
