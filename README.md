# FastAPI + PostgreSQL CRUD (Tasks)

Мини-проект: REST API на **FastAPI** с хранением данных в **PostgreSQL**.  
Есть **CRUD**, **Swagger документация**, **SQLAlchemy 2.0** и **Alembic миграции**.

## Стек
- FastAPI
- PostgreSQL (Docker)
- SQLAlchemy 2.0
- psycopg (driver)
- Alembic (migrations)
- Pydantic

---

## 🚀 Запуск проекта

### 1) Поднять PostgreSQL в Docker
```bash
docker run --name pg-fastapi \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=pass \
  -e POSTGRES_DB=appdb \
  -p 5432:5432 \
  -d postgres:16