from google.adk import Agent
from app.tools import TOOLS

def execute_tools(plan: dict):
    results = []
    workflow = []

    for action in plan.get("actions", []):
        tool = action.get("tool")
        payload = action.get("input", {})

        workflow.append(f"transfer_to_agent → {tool}")

        if tool not in TOOLS:
            results.append({"tool": tool, "status": "not_found"})
            continue

        result = TOOLS[tool](payload)

        workflow.append(f"{tool} executed")

        results.append({
            "tool": tool,
            "result": result
        })

    return {
        "results": results,
        "workflow": workflow
    }

executor_agent = Agent(
    name="executor",
    model="gemini-2.5-flash",
    description="Executes planned actions using tools",
    tools=[execute_tools],
    output_key="execution"
)