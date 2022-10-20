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
Testing
```
make test
```
Manual Testing
```
make generate_file
make celery_worker
make shell
  # in shell: from parse_large_file.tasks import import_file_task; import_file_task.apply_async()
make runserver
  # open http://127.0.0.1:8000/customers-age/
  # open http://127.0.0.1:8000/customers/
```
Other commands

```
make bash
make migrations
make test_new_db
```

ToDo

- unit test
  - test api results
  - test task with celery always eager true


- move rabbitmq initial config to dockerfile
  - add secrets file
-------
- add django SECRET_KEY to env
- Add secrets file
- Update mysql user
