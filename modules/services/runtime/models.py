from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class LLMModel(BaseModel):
    id: str
    name: str
    provider: str

class RuntimeBase(BaseModel):
    name: str
    agent_id: str
    models: List[LLMModel]

class RuntimeCreate(RuntimeBase):
    pass

class RuntimeUpdate(BaseModel):
    name: Optional[str] = None
    agent_id: Optional[str] = None
    models: Optional[List[LLMModel]] = None

class Runtime(RuntimeBase):
    id: str
    status: str = "stopped"
