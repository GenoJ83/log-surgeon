from typing import List
from src.models.entry import LogEntry

def generate_html_report(entries: List[LogEntry]) -> str:
    rows = ''.join(f'<tr><td>{e.timestamp}</td><td>{e.level}</td><td>{e.message}</td></tr>' for e in entries)
    return f'<html><head><style>body{{font-family:sans-serif;}}table{{border-collapse:collapse;width:100%;}}td,th{{border:1px solid #ddd;padding:8px;}}</style></head><body><h2>LogSurgeon Report</h2><table><tr><th>Timestamp</th><th>Level</th><th>Message</th></tr>{rows}</table></body></html>'
