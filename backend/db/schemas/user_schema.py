from pydantic import BaseModel
from typing import List
from datetime import datetime
from db.schemas.note_schema import Note


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    notes: List[Note] = []
    updated_at: datetime
    created_at: datetime

    class Config:
        orm_mode = True
