from google.adk import Agent

formatter_agent = Agent(
    name="formatter",
    model="gemini-2.5-flash",
    description="Formats final response",
    instruction="""
    Convert EXECUTION into a user-friendly response.

    EXECUTION:
    { execution }
    """
)