import sqlite3

DB_FILE = "agent.db"

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  # makes output nicer
    return conn