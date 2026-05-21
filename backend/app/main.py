from fastapi import FastAPI

app=FastAPI()

@app.get("/")

def home():
    return {"message":"AI Scholorship assistant API running"}