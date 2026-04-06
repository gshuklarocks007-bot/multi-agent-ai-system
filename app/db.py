import psycopg2
from app.config import *

def get_db_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=f"/cloudsql/{INSTANCE_CONNECTION_NAME}"
    )