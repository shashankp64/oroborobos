from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class AgentBase(BaseModel):
    name: str
    description: str
    prompt: str
    tools: List[str]  # List of tool IDs

class AgentCreate(AgentBase):
    pass

class AgentUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    prompt: Optional[str] = None
    tools: Optional[List[str]] = None

class Agent(AgentBase):
    id: str
