ToDo

- create model
  - SampleUsers
    - email - unique, not null
    - age
    - added_at
    - first_name
    - username
- create api
  - get count user group by age
  - get user order by added_at

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
- Add secrets file