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

shell:
	docker exec -i -t backend bash

migrations:
	docker exec -t backend python manage.py migrate makemigrations

migrate:
	docker exec -t backend python manage.py migrate
