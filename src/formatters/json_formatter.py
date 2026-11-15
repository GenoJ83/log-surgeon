import json
from typing import List
from src.models.entry import LogEntry

def format_json(entries: List[LogEntry]) -> str:
    return json.dumps([e.model_dump() for e in entries], indent=2)
