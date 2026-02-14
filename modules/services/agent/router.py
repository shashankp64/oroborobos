from fastapi import APIRouter, Depends
from typing import List
from .models import Agent, AgentCreate, AgentUpdate
from modules.persistence.interface import StorageInterface

async def get_storage():
    pass

router = APIRouter()

@router.get("/", response_model=List[Agent])
async def list_agents(storage: StorageInterface = Depends(get_storage)):
    """List all agents."""
    pass

@router.post("/", response_model=Agent)
async def create_agent(agent: AgentCreate, storage: StorageInterface = Depends(get_storage)):
    """Create a new agent."""
    pass

@router.get("/{agent_id}", response_model=Agent)
async def get_agent(agent_id: str, storage: StorageInterface = Depends(get_storage)):
    """Get an agent by ID."""
    pass

@router.put("/{agent_id}", response_model=Agent)
async def update_agent(agent_id: str, agent: AgentUpdate, storage: StorageInterface = Depends(get_storage)):
    """Update an agent."""
    pass

@router.delete("/{agent_id}")
async def delete_agent(agent_id: str, storage: StorageInterface = Depends(get_storage)):
    """Delete an agent."""
    pass
