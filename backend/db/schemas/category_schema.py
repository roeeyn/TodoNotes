from pydantic import BaseModel
from typing import List
from db.schemas.note_schema import Note
from datetime import datetime


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    updated_at: datetime
    created_at: datetime
    notes: List[Note] = []

    class Config:
        orm_mode = True
