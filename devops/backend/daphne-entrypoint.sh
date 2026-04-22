#!/bin/sh

set -eu

. /code/devops/backend/common-entrypoint.sh

require_command daphne
exec_in_app daphne -b 0.0.0.0 -p 8001 config.asgi:application
