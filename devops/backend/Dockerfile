# ── Stage 1: builder ─────────────────────────────────────────────────────────
FROM python:3.13-slim-bookworm AS builder

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/app/.venv

COPY --from=ghcr.io/astral-sh/uv:0.6 /uv /uvx /usr/local/bin/

WORKDIR /app

COPY pyproject.toml .
RUN uv sync --no-dev --no-install-project

# ── Stage 2: runtime ─────────────────────────────────────────────────────────
FROM python:3.13-slim-bookworm AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /code/backend

COPY --from=builder /app/.venv /app/.venv

COPY ./backend /code/backend
