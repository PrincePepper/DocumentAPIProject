запустить локально api, без бд:

`uvicorn app.main:app --reload --debug`

Запустить все сразу через докер:

1. docker build -t fastapi .
2. docker compose --env-file .env up -d

Файл .env:

```dotenv
DB_USERNAME=admin
DB_PASSWORD=admin
DB_DATABASE=test_database
DB_HOST=db
DB_PORT=5432
DB_POSTGRES_HOST=localhost
PGADMIN_PORT=5050
PGADMIN_DEFAULT_EMAIL=pgadmin4@pgadmin.org
PGADMIN_DEFAULT_PASSWORD=admin
```

localhost:8000-fastapi
localhost:5050-pgadmin
