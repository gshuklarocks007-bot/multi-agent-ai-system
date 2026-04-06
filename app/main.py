from fastapi import FastAPI
from app.agent import execute_workflow

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/chat")
def chat(input: str):
    return execute_workflow(input)