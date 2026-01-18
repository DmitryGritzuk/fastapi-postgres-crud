# FastAPI + Postgres CRUD (Tasks)

Мини-проект: CRUD API на FastAPI + PostgreSQL + SQLAlchemy + Alembic.

## Стек
- FastAPI
- PostgreSQL (Docker)
- SQLAlchemy 2.0
- psycopg (driver)
- Alembic (миграции)
- Pydantic v2

## Запуск

### 1) База данных (Docker)
```bash
docker run --name pg-fastapi \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=pass \
  -e POSTGRES_DB=appdb \
  -p 5432:5432 \
  -d postgres:16