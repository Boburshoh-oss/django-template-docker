#!/bin/sh

set -eu

APP_DIR=${APP_DIR:-/code/backend}
DB_HOST=${DB_HOSTNAME:-db}
DB_PORT_NUMBER=${DB_PORT:-5432}

log() {
    printf '%s\n' "$*"
}

require_command() {
    if ! command -v "$1" >/dev/null 2>&1; then
        >&2 printf '%s\n' "Required command not found: $1"
        exit 1
    fi
}

cd_app() {
    cd "$APP_DIR"
}

wait_for_postgres() {
    require_command nc
    log "Waiting for PostgreSQL at ${DB_HOST}:${DB_PORT_NUMBER}..."

    until nc -z "$DB_HOST" "$DB_PORT_NUMBER"; do
        sleep 1
    done

    log "PostgreSQL is available"
}

run_manage_command() {
    require_command python
    cd_app
    python manage.py "$@"
}

collect_static() {
    run_manage_command collectstatic --no-input
}

run_migrations() {
    run_manage_command migrate --no-input
}

exec_in_app() {
    cd_app
    exec "$@"
}