import json
from app.tools import *
from app.db import get_db_connection

# IAM POLICY
USER_PERMISSIONS = {
    "task.get": True,
    "task.create": True,
    "calendar.get": True,
    "calendar.create": True,
    "notes.create": True,
    "calendar.delete": False
}

# TOOL REGISTRY
TOOLS = {
    "task.get": lambda: get_tasks(),
    "task.create": lambda payload: create_task(payload),
    "calendar.get": lambda: get_events(),
    "calendar.create": lambda payload: create_event(payload),
    "notes.create": lambda payload: create_note(payload),
}

# IAM CHECK
def is_action_allowed(action):
    return USER_PERMISSIONS.get(action, False)

# SAFE EXECUTION
def safe_execute(tool, payload):
    try:
        if payload:
            return TOOLS[tool](payload)
        return TOOLS[tool]()
    except Exception as e:
        return f"Fallback: {str(e)}"

# PREFERENCES
def update_preference(key, value):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO user_preferences (user_id, key, value) VALUES (1, %s, %s)",
        (key, value)
    )
    conn.commit()
    conn.close()

# PRIMARY AGENT (SIMPLIFIED)
def primary_agent(user_input):
    user_input = user_input.lower()

    # ❌ DELETE (blocked / unsupported)
    if "delete" in user_input:
        return {
            "actions": [
                {
                    "tool": "calendar.delete"
                }
            ]
        }

    # ✅ SHOW TASKS
    if "task" in user_input:
        return {"actions": [{"tool": "task.get"}]}

    # ✅ CREATE MEETING
    if "schedule" in user_input or "create meeting" in user_input:
        return {
            "actions": [
                {
                    "tool": "calendar.create",
                    "input": {
                        "title": "Meeting",
                        "datetime": "2026-04-07 17:00"
                    }
                },
                {
                    "tool": "notes.create",
                    "input": {
                        "content": "Meeting scheduled"
                    }
                }
            ]
        }

    return {"actions": []}

# EXECUTOR
def execute_workflow(user_input):
    decision = primary_agent(user_input)
    results = []

    for action in decision["actions"]:
        tool = action["tool"]
        payload = action.get("input")

        if not is_action_allowed(tool):
            results.append({"tool": tool, "status": "blocked"})
            continue

        result = safe_execute(tool, payload)

        results.append({
            "tool": tool,
            "result": result,
            "reason": f"Based on user input: {user_input}"
        })

    return {"results": results}
