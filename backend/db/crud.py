
from sqlalchemy.orm import Session
from db.schemas.user_schema import UserCreate
from db.schemas.note_schema import NoteCreate
from db.schemas.category_schema import CategoryCreate
from db.models import User, Note, Category
from auth.auth_utils import get_password_hash
from sqlalchemy import or_

def create_user(db: Session, user: UserCreate):
    user.password = get_password_hash(user.password)
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email_or_username(db: Session, email: str, username: str = None):
    return db.query(User).filter(or_(User.email == email, User.username == username)).first()

def create_user_note(db: Session, note:NoteCreate):
    db_item = Note(**note.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_user_notes(db: Session, user_id: int):
    return (
        db.query(
            Note.id,
            Note.title,
            Note.description,
            Note.status, 
            Note.deadline,
            Note.category_id,
            Note.user_id,
            Note.created_at,
            Note.updated_at,
            Category.name.label("category_name")
        )
        .join(Category, Category.id == Note.category_id)
        .filter(Note.user_id == user_id).all())


def create_category(db: Session, category: CategoryCreate):
    db_item = Category(**category.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
