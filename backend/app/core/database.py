from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL="postgresql://postgres:abc@localhost:5432/scholarship_ai"

engine=create_engine(DATABASE_URL)

SessionLocal=sessionmaker(
    autocomplete=False,
    autoflush=False,
    bind=engine
)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield  db
    finally:
        db.close()

