from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

db_user = os.getenv("DB_USER", "root")
db_password = os.getenv("DB_PASSWORD", "root")
db_host = os.getenv("DB_HOST", "localhost")
db_schema = os.getenv("DB_SCHEMA", "TODO_NOTES")

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_schema}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
