from sqlalchemy import create_engine
from sqlalchemy import sessionmaker, declarative_base

DATABASE_URL="postgresql://postgres:abc@localhost:5432/scholorship_ai"

engine=create_engine(DATABASE_URL)

SessionLocal=sessionmaker(bind=engine)

Base=declarative_base()

