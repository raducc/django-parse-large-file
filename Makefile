build:
	docker-compose build

init_rabbitmq:
	docker exec -t rabbitmq rabbitmqctl add_vhost large_file
	docker exec -t rabbitmq rabbitmqctl add_user admin password123
	docker exec -t rabbitmq rabbitmqctl set_permissions -p large_file admin ".*" ".*" ".*"
	docker exec -t rabbitmq rabbitmqctl set_user_tags admin administrator

up:
	docker-compose up -d

down:
	docker-compose down

bash:
	docker exec -i -t backend bash

shell:
	docker exec -i -t backend python manage.py shell

migrations:
	docker exec -t backend python manage.py makemigrations

migrate:
	docker exec -t backend python manage.py migrate

celery_worker:
	docker exec -t backend celery -A parse_large_file worker -l info

runserver:
	docker exec -t backend python manage.py runserver 0.0.0.0:8000

test_new_db:
	docker exec -i -t backend python manage.py test

test:
	docker exec -t backend python manage.py test --keepdb

generate_file:
	docker exec -t backend python manage.py generate_file --lines 10000
