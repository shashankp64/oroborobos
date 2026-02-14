from pydantic import BaseModel
from typing import List, Optional, Dict, Any

from enum import Enum

class LLMModel(BaseModel):
    id: str
    name: str
    provider: str

class EnvironmentType(str, Enum):
    LOCAL = "local"
    # Future types can be added here, e.g., DOCKER, K8S

class Environment(BaseModel):
    type: EnvironmentType
    config: Dict[str, Any] = {}

class RuntimeBase(BaseModel):
    name: str
    environment: Environment
    models: List[LLMModel]

class RuntimeCreate(RuntimeBase):
    pass

class RuntimeUpdate(BaseModel):
    name: Optional[str] = None
    environment: Optional[Environment] = None
    models: Optional[List[LLMModel]] = None

class Runtime(RuntimeBase):
    id: str
    status: str = "stopped"
