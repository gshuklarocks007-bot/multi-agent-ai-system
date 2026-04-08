from app.db import get_connection

def get_tasks():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def create_event(payload):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO events (title, datetime) VALUES (?, ?)",
        (payload.get("title"), payload.get("datetime"))
    )

    conn.commit()
    conn.close()
    return "Event created"

def create_note(payload):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO notes (content) VALUES (?)",
        (payload.get("content"),)
    )

    conn.commit()
    conn.close()
    return "Note created"

TOOLS = {
    "task.get": get_tasks,
    "calendar.create": create_event,
    "notes.create": create_note,
}