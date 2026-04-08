from google.adk import Agent

planner_agent = Agent(
    name="planner",
    model="gemini-2.5-flash",
    description="Plans actions based on user input",
    instruction="""
    Analyze PROMPT and return JSON:

    Example:
    {
      "actions": [
        {"tool": "calendar.create", "input": {"title": "Meeting", "datetime": "2026-04-07 17:00"}}
      ]
    }

    PROMPT:
    { PROMPT }
    """,
    output_key="plan"
)