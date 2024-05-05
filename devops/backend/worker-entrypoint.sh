#!/bin/sh

until cd /code/backend
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A config worker --loglevel=info  -E 
