from app.db import get_db_connection

# TASKS
def get_tasks():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, status FROM tasks WHERE status='pending'")
    result = cur.fetchall()
    conn.close()
    return [dict(row) for row in result]


def create_task(payload):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tasks (user_id, title, status) VALUES (?, ?, ?)",
        (1,payload["title"],'pending')
    )
    conn.commit()
    conn.close()
    return "Task created"


# CALENDAR
def get_events():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, datetime FROM events")
    result = cur.fetchall()
    conn.close()
    return [dict(row) for row in result]


def create_event(payload):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO events (user_id, title, datetime) VALUES (?, ?, ?)",
        (1,payload["title"], payload["datetime"])
    )
    conn.commit()
    conn.close()
    return "Event created"


# NOTES
def create_note(payload):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO notes (user_id, content) VALUES (?,?)",
        (1,payload["content"])
    )
    conn.commit()
    conn.close()
    return "Note created"