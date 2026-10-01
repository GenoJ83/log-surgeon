from src.models.entry import LogEntry

def parse_syslog(line: str) -> LogEntry:
    parts = line.split(maxsplit=4)
    if len(parts) >= 5:
        return LogEntry(timestamp=f'{parts[0]} {parts[1]} {parts[2]}', source=parts[3], message=parts[4])
    return LogEntry(message=line)
