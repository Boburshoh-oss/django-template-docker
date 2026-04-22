FROM python:3.12-slim-bookworm

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /code

COPY ./requirements.txt .


RUN apt-get update -y \
    && apt-get install -y --no-install-recommends netcat-openbsd \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

COPY ./backend /code/backend
COPY ./devops /code/devops

RUN chmod +x /code/devops/backend/common-entrypoint.sh \
    && chmod +x /code/devops/backend/server-entrypoint.sh
# RUN chmod +x /code/devops/backend/worker-entrypoint.sh
RUN chmod +x /code/devops/backend/local-entrypoint.sh
RUN chmod +x /code/devops/backend/daphne-entrypoint.sh
# RUN chmod +x /code/devops/backend/flower-entrypoint.sh
