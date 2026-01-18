from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    is_done: Optional[bool] = None


class TaskOut(BaseModel):
    id: int
    title: str
    is_done: bool
    created_at: datetime

    class Config:
        from_attributes = True


class TaskOut(BaseModel):
    id: int
    title: str
    is_done: bool
    created_at: datetime

    model_config = {"from_attributes": True}        