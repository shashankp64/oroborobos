from pydantic import BaseModel
from typing import Dict, Any, Optional, List
from enum import Enum

class ToolType(str, Enum):
    PYTHON = "python"
    API = "api"
    MCP = "mcp"
    OTHER = "other"

class ToolBase(BaseModel):
    name: str
    description: str
    type: ToolType
    config: Dict[str, Any]

class ToolCreate(ToolBase):
    pass

class ToolUpdate(BaseModel):
    description: Optional[str] = None
    type: Optional[ToolType] = None
    config: Optional[Dict[str, Any]] = None

class Tool(ToolBase):
    id: str
