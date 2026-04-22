# Django Template Docker

Production-oriented Django template with Docker for local development, a separate production compose stack, and ready-to-use GitHub Actions automation.

## Stack

- Python 3.13
- Django 6 + Django REST Framework
- PostgreSQL 18
- Redis 7
- Uvicorn + Nginx
- uv for dependency management
- drf-spectacular for OpenAPI schema and docs

## What This Template Includes

- Docker Compose setup for development and production
- Split Django settings for development and production
- Custom user model with JWT authentication support
- Redis cache configuration
- OpenAPI schema generation with Swagger and ReDoc
- GitHub Actions CI for linting and tests
- GitHub Actions CD for publishing Docker images to GHCR

## Quick Start

1. Copy the sample environment file.
2. Start the local services.
3. Apply migrations.

```bash
cp .env.example .env
docker compose up --build -d
docker compose run --rm migrate
```

Application endpoints:

- Django app: `http://127.0.0.1:8000`
- OpenAPI schema: `http://127.0.0.1:8000/api/schema/`
- Swagger UI: `http://127.0.0.1:8000/api/docs/`
- ReDoc: `http://127.0.0.1:8000/api/redoc/`

## Local Development

Start the development stack:

```bash
docker compose up --build
```

Run management commands inside the app container:

```bash
docker compose exec web python manage.py createsuperuser
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
```

Stop and remove containers:

```bash
docker compose down
```

Start the production-like stack locally:

```bash
docker compose -f docker-compose.prod.yml up --build
```

## Local Quality Checks

If you want to run checks without Docker, install dependencies with `uv`:

```bash
uv sync --extra dev
uv run ruff check backend
uv run pytest
```

## CI/CD

This template now includes two GitHub Actions workflows:

- `ci.yml`: runs `ruff` and `pytest` on pushes and pull requests using PostgreSQL and Redis service containers.
- `cd.yml`: builds and publishes `backend` and `nginx` Docker images to GitHub Container Registry on every push to `main` and on manual dispatch.

Published image names follow this pattern:

```text
ghcr.io/<owner>/<repository>/backend
ghcr.io/<owner>/<repository>/nginx
```

The provided CD workflow is a template-friendly baseline. It handles image publishing, while the final deployment step should be adapted to your hosting environment.

## Environment Notes

Important variables in `.env`:

- `DEBUG`: enables development-only behavior such as Debug Toolbar
- `DJANGO_SETTINGS_MODULE`: `config.settings.development` or `config.settings.production`
- `ALLOWED_HOSTS`: comma-separated host list
- `CSRF_TRUSTED_ORIGINS`: comma-separated origins including scheme
- `DB_HOSTNAME`, `DB_NAME`, `DB_USERNAME`, `DB_PASSWORD`, `DB_PORT`: PostgreSQL connection settings
- `REDIS_URL`: Redis connection string
- `SENTRY_DSN`: optional production error reporting

Production security flags are intentionally environment-controlled so this template can run behind different proxy and TLS setups.

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

