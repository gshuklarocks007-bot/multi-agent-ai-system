import os

DB_NAME = os.getenv("DB_NAME", "agentdb")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
INSTANCE_CONNECTION_NAME = os.getenv("INSTANCE_CONNECTION_NAME")

PROJECT_ID = os.getenv("PROJECT_ID")
REGION = os.getenv("REGION", "asia-south1")