build:
	docker network create kong-net || true
	docker build -t kong_nodb ./kong
	docker-compose build

run: build
	docker-compose up

cleanup:
	docker-compose down

check: build
	docker-compose -p tests run mysite python3 manage.py makemigrations
	docker-compose -p tests run mysite python3 manage.py migrate
	docker-compose -p tests run mysite python3 manage.py test

restartkong:
	docker-compose down kong
	docker build -t kong_nodb ./kong
	docker-compose up kong