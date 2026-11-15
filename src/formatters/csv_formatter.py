import csv
import io
from typing import List
from src.models.entry import LogEntry

def format_csv(entries: List[LogEntry]) -> str:
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['timestamp', 'level', 'source', 'message'])
    for e in entries:
        writer.writerow([e.timestamp, e.level, e.source, e.message])
    return output.getvalue()
