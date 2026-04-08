from google.adk.agents import SequentialAgent
from app.agents.planner_agent import planner_agent
from app.agents.executor_agent import executor_agent
from app.agents.formatter_agent import formatter_agent

workflow = SequentialAgent(
    name="multi_agent_workflow",
    sub_agents=[
        planner_agent,
        executor_agent,
        formatter_agent
    ]
)

def run_workflow(prompt: str):
    state = {"PROMPT": prompt}
    result = workflow.invoke(state)
    return result