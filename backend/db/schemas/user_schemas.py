from pydantic import BaseModel
from typing import List
import datetime
from db.schemas.note_schema import Note


class UserBase(BaseModel):
    username: str
    email: str
    updated_at: datetime
    created_at: datetime


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    notes: List[Note] = []

    class Config:
        orm_mode = True
