from google.adk import Agent
from multi_agent_ai_system.app.workflow import workflow

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    description="Main entry point",
    instruction="Delegate user request to workflow",
    sub_agents=[workflow]
)