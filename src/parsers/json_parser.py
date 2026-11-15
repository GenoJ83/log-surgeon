import json
from src.models.entry import LogEntry

def parse_json_line(line: str) -> LogEntry:
    try:
        data = json.loads(line)
        return LogEntry(timestamp=data.get('timestamp'), level=data.get('level', 'INFO'), message=data.get('message', ''), metadata=data)
    except json.JSONDecodeError:
        return LogEntry(message=line)
