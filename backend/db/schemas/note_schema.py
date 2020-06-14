from pydantic import BaseModel
from typing import List
import datetime


class NoteBase(BaseModel):
    title: str
    description: str
    status: int
    deadline: datetime
    category_id: int
    user_id: str
    created_at: datetime
    updated_at: datetime


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int

    class Config:
        orm_mode = True
