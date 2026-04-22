#!/bin/sh

set -eu

. /code/devops/backend/common-entrypoint.sh

require_command timeout
require_command celery
cd_app

until timeout 10 celery -A config inspect ping; do
    >&2 printf '%s\n' 'Celery workers not available'
    sleep 1
done

exec celery -A config flower --port=5555 --persistent=True
