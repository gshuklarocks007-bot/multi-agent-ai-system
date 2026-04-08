from google.adk import Agent
from app.workflow import workflow

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    description="Main entry point for the multi-agent system",
    instruction="""
    Accept user input and delegate to workflow.
    """,
    sub_agents=[workflow]
)