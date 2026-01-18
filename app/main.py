from __future__ import annotations

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .db import get_db
from . import crud, schemas

app = FastAPI(title="FastAPI + Postgres CRUD (Tasks)", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tasks", response_model=schemas.TaskOut, status_code=201)
def create_task(payload: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, payload)


@app.get("/tasks", response_model=list[schemas.TaskOut])
def list_tasks(limit: int = 50, offset: int = 0, db: Session = Depends(get_db)):
    limit = max(1, min(100, limit))
    offset = max(0, offset)
    return crud.list_tasks(db, limit=limit, offset=offset)


@app.get("/tasks/{task_id}", response_model=schemas.TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.patch("/tasks/{task_id}", response_model=schemas.TaskOut)
def patch_task(task_id: int, payload: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return crud.update_task(db, task, payload)


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    crud.delete_task(db, task)
    return None