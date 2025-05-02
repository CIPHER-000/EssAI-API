from fastapi import APIRouter, Body
from pydantic import BaseModel
from app.services.agent_runner import run_agent

router = APIRouter()

class AgentInput(BaseModel):
    prompt: str

@router.post("/run-agent")
def handle_agent_request(data: AgentInput):
    return {"result": run_agent(data.prompt)}
