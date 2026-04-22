# Django Template Docker

Minimal Django + DRF template with Docker-based local development and a production compose stack. The template has been refreshed for a more modern workflow: current Python base image, Compose v2 commands, healthchecks, environment-driven settings, and safer debug/prod defaults.

## Stack

- Python 3.12
- Django + Django REST Framework
- PostgreSQL 16
- Gunicorn + Nginx for production compose
- drf-yasg for API docs

## What Was Modernized

- Docker image moved to `python:3.12-slim-bookworm`
- Compose services now use `depends_on.condition` with PostgreSQL healthchecks
- Django settings now read list/bool values from environment variables
- `debug_toolbar` and debug routes load only when `DEBUG=True`
- `manage.py` now respects `DJANGO_SETTINGS_MODULE` from the environment
- Make targets use `docker compose` instead of deprecated `docker-compose`

## Quick Start

1. Copy the sample environment file.
2. Start the development stack.
3. Run migrations.

```bash
cp .env-example .env
make dev-up
docker compose -f docker-compose.yml exec web python backend/manage.py migrate
```

Application endpoints:

- Django app: `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/swagger/`
- ReDoc: `http://127.0.0.1:8000/redoc/`

## Common Commands

```bash
make dev-up
make dev-down
make prod-up
make prod-down
make makemigrations
make migrate
make createsuperuser
make logs
```

## Environment Notes

Important variables in `.env`:

- `DEBUG`: toggles debug-only tooling like Django Debug Toolbar
- `ALLOWED_HOSTS`: comma-separated list
- `CORS_ALLOWED_ORIGINS`: comma-separated list when `CORS_ALLOW_ALL_ORIGINS=False`
- `CSRF_TRUSTED_ORIGINS`: comma-separated list with scheme, for example `http://localhost:8000`
- `DJANGO_SETTINGS_MODULE`: `config.settings.development` or `config.settings.production`

Production security flags are intentionally environment-controlled so the same template can run behind or without a TLS-terminating proxy.

## Project Layout

```text
backend/
	apps/
	config/
devops/
	backend/
	nginx/
frontend/
templates/
```

## Next Improvements

- Replace `drf-yasg` with `drf-spectacular` if you want OpenAPI 3-first schema generation
- Add Celery/Redis services only if the project actually uses async jobs
- Add CI for linting, tests, and image builds

## Entrypoint Notes

Backend service scripts now share a common helper in `devops/backend/common-entrypoint.sh`. They use strict shell mode, wait for PostgreSQL only when needed, and end with `exec` so signals reach the main process correctly inside containers.

The Celery worker and Flower scripts are kept as optional entrypoints. If you enable them, make sure Celery is installed and wired into the project first.

