import re
from src.models.entry import LogEntry

DEFAULT_PATTERN = re.compile(r'^\[(?P<timestamp>[^\]]+)\]\s+(?P<level>\w+):\s+(?P<message>.*)$')

def parse_line(line: str) -> LogEntry:
    m = DEFAULT_PATTERN.match(line.strip())
    if m:
        return LogEntry(**m.groupdict())
    return LogEntry(message=line.strip())
