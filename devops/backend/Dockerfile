FROM python:3.12.4-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements.txt .


RUN apt-get update -y \
    && apt-get install -y netcat \
    # Keraksiz paketlarni va apt-get listlarini tozalashni birlashtirish
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip \
    && pip install -r requirements.txt --no-cache-dir

ADD ./backend /code/backend
ADD ./devops /code/devops

RUN chmod +x /code/devops/backend/server-entrypoint.sh
# RUN chmod +x /code/devops/backend/worker-entrypoint.sh
RUN chmod +x /code/devops/backend/local-entrypoint.sh
RUN chmod +x /code/devops/backend/daphne-entrypoint.sh
# RUN chmod +x /code/devops/backend/flower-entrypoint.sh
