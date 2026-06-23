from pydantic import BaseModel
from typing import Dict, Any


class ToolMetadata(BaseModel):
    name: str
    description: str
    input_schema: Dict[str, Any]