from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine,Base

from app.models import *

app=FastAPI()

Base.metadata.create_all(bind=engine) #Creates tables automatically in PostgreSQL.

origins=[
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")

def root():
    return {"message":"AI Scholorship assistant API running"}