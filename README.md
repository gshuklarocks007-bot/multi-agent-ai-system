# Multi-Agent AI System (ADK + Gemini 2.5 Flash)

## Features
- Multi-agent orchestration (Planner → Executor → Formatter)
- SQLite database integration
- Workflow visualization (ADK UI)
- Cloud Run deployment

## Run locally
pip install -r requirements.txt  
uvicorn app.main:app --reload

## Deploy
uvx --from google-adk==1.14.0 adk deploy cloud_run ...