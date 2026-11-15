from pydantic import BaseModel
from typing import Optional, Dict, Any

class LogEntry(BaseModel):
    timestamp: Optional[str] = None
    level: str = 'INFO'
    message: str
    source: Optional[str] = None
    metadata: Dict[str, Any] = {}
