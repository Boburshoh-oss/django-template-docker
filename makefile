command:
	echo "command"

user:
	docker-compose -f docker-compose.prod.yml run --rm web python backend/manage.py createsuperuser

up:
	docker-compose -f docker-compose.prod.yml up --build -d

down:
	docker-compose -f docker-compose.prod.yml down

migrate:
	docker-compose -f docker-compose.prod.yml run --rm web python backend/manage.py makemigrations
	docker-compose -f docker-compose.prod.yml run --rm web python backend/manage.py migrate
