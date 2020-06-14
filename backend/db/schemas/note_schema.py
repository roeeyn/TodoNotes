from pydantic import BaseModel
from typing import List
from datetime import datetime


class NoteBase(BaseModel):
    title: str
    description: str
    status: int = 0
    user_id: int = -1
    deadline: datetime
    category_id: int


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int
    updated_at: datetime
    created_at: datetime
    category_name: str = None

    class Config:
        orm_mode = True
