from fastapi import FastAPI
from app.agent import execute_workflow
from app.init_db import init_db

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def home():
    return {"status": "Multi-agent AI system running"}

@app.post("/chat")
def chat(input: str):
    return execute_workflow(input)