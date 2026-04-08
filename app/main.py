from fastapi import FastAPI
from app.workflow import run_workflow
from app.init_db import init_db

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

@app.post("/chat")
def chat(input: str):
    return run_workflow(input)