from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Task
from .schemas import TaskCreate, TaskUpdate


def create_task(db: Session, data: TaskCreate) -> Task:
    t = Task(title=data.title)
    db.add(t)
    db.commit()
    db.refresh(t)
    return t


def get_task(db: Session, task_id: int):
    return db.get(Task, task_id)


def list_tasks(db: Session, limit: int = 50, offset: int = 0) -> list[Task]:
    stmt = select(Task).order_by(Task.id.desc()).limit(limit).offset(offset)
    return list(db.execute(stmt).scalars().all())


def update_task(db: Session, task: Task, data: TaskUpdate) -> Task:
    if data.title is not None:
        task.title = data.title
    if data.is_done is not None:
        task.is_done = data.is_done
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: Task) -> None:
    db.delete(task)
    db.commit()