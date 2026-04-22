COMPOSE_DEV = docker compose -f docker-compose.yml
COMPOSE_PROD = docker compose -f docker-compose.prod.yml

.PHONY: help dev-up dev-down prod-up prod-down migrate makemigrations createsuperuser logs

help:
	@echo "Available targets: dev-up dev-down prod-up prod-down migrate makemigrations createsuperuser logs"

dev-up:
	$(COMPOSE_DEV) up --build -d

dev-down:
	$(COMPOSE_DEV) down

prod-up:
	$(COMPOSE_PROD) up --build -d

prod-down:
	$(COMPOSE_PROD) down

migrate:
	$(COMPOSE_PROD) run --rm web python backend/manage.py migrate

makemigrations:
	$(COMPOSE_PROD) run --rm web python backend/manage.py makemigrations

createsuperuser:
	$(COMPOSE_PROD) run --rm web python backend/manage.py createsuperuser

logs:
	$(COMPOSE_DEV) logs -f web db
