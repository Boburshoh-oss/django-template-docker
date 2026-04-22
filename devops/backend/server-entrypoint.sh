#!/bin/sh

set -eu

. /code/devops/backend/common-entrypoint.sh

wait_for_postgres
run_migrations
collect_static

require_command gunicorn
exec_in_app gunicorn config.wsgi:application --bind 0.0.0.0:8000
