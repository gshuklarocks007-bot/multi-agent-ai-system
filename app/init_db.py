from app.db import get_db_connection

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()

    with open("schema.sql", "r") as f:
        cur.executescript(f.read())

    conn.commit()
    conn.close()