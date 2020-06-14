from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    DefaultClause,
    DateTime,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    updated_at = Column(DateTime, DefaultClause(func.now(), for_update=True))
    created_at = Column(DateTime, DefaultClause(func.now()))
    notes = relationship("Note", backref="users")


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    # 0: Por hacer
    # 1: Haciendo
    # 2: Hecho
    status = Column(Integer, default=0)
    deadline = Column(DateTime)
    category_id = Column(Integer, ForeignKey("categories.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    updated_at = Column(DateTime, DefaultClause(func.now(), for_update=True))
    created_at = Column(DateTime, DefaultClause(func.now()))


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    updated_at = Column(DateTime, DefaultClause(func.now(), for_update=True))
    created_at = Column(DateTime, DefaultClause(func.now()))
    notes = relationship("Note", backref="categories")
