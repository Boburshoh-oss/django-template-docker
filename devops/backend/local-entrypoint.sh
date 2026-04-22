#!/bin/sh

set -eu

. /code/devops/backend/common-entrypoint.sh

wait_for_postgres
collect_static

require_command python
exec_in_app python manage.py runserver 0.0.0.0:8000


