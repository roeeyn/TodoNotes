import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status, Request, Response, Cookie

from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from db.schemas.user_schema import User, UserCreate
from db.schemas.note_schema import Note, NoteCreate
from db.schemas.category_schema import Category, CategoryCreate
from typing import List

from auth.auth import authenticate_user, create_access_token
from auth.auth_schema import Token
from db import models, crud
from db.database import SessionLocal, engine

from fastapi.security import OAuth2PasswordRequestForm

from auth.auth import get_current_active_user, get_admin_user

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

# # Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def health_check():
    return {"status": "cool 😎"}


@app.post("/token", response_model=Token)
async def login_for_access_token(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user.email})
    response.set_cookie(key="tn_cookie", value=access_token.decode("utf-8"))
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/me", response_model=User)
async def get_me(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    db_user = crud.get_user_by_id(db, user_id=current_user.id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users", response_model=User)
def create_user(
    user: UserCreate, db: Session = Depends(get_db),
):
    db_user = crud.get_user_by_email_or_username(
        db, email=user.email, username=user.username
    )
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/note", response_model=List[Note])
def get_user_notes(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)
):
    return crud.get_user_notes(db, current_user.id)


@app.post("/note", response_model=Note)
def create_note_for_user(
    note: NoteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    note.user_id = current_user.id
    return crud.create_user_note(db, note)


@app.post("/category", response_model=Category)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    return crud.create_category(db, category)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
