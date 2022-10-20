How to use
  
Ensure `docker` is running then run the following command in terminal
```
make build
make up
make init_rabbitmq
make migrate
```

To stop docker-compose run
```
make down
```

Other commands

```
make celery_worker
make bash
make shell
make migrations
make runserver
make test
```

ToDo

- unit test
  - test util with random file
    - test that entries are created in db
  - test api results

- bottleneck on writing to the db. Possible solutions:
  - bulk update or create
  - spawn tasks to write to db

- move rabbitmq initial config to dockerfile
  - add secrets file
-------
- add django SECRET_KEY to env
- Add secrets file
- Update mysql user
