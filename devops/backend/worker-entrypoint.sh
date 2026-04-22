#!/bin/sh

set -eu

. /code/devops/backend/common-entrypoint.sh

require_command celery
exec_in_app celery -A config worker --loglevel=info -E
