from google.adk import Agent
from google.adk.tools.tool_context import ToolContext

def save_prompt(tool_context: ToolContext, prompt: str):
    tool_context.state["PROMPT"] = prompt
    return {"status": "saved"}

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    description="Entry agent that captures user input",
    instruction="""
    Save the user prompt into state and pass control to workflow.
    """,
    tools=[save_prompt],
)