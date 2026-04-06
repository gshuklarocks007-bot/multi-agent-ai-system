# 🚀 Multi-Agent AI System (Google Cloud)

## 🔥 Overview

A policy-aware multi-agent AI system that:

* Coordinates multiple agents (Task, Calendar, Notes)
* Uses IAM-based security
* Learns user preferences
* Executes workflows autonomously

## 🧠 Features

* Multi-agent orchestration
* IAM policy enforcement
* Self-learning memory
* Explainable AI responses
* Shadow simulation mode

## 🏗️ Architecture

Cloud Run → Agent → Tools → Cloud SQL

## ⚙️ Tech Stack

* FastAPI
* PostgreSQL (Cloud SQL)
* Google Cloud Run
* Vertex AI (extendable)

## 🚀 Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## ☁️ Deploy

```bash
gcloud run deploy
```