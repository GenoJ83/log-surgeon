from typing import List
from src.models.entry import LogEntry

class LogFilter:
    def __init__(self, level: str = None, keyword: str = None):
        self.level = level.upper() if level else None
        self.keyword = keyword.lower() if keyword else None

    def matches(self, entry: LogEntry) -> bool:
        if self.level and entry.level != self.level:
            return False
        if self.keyword and self.keyword not in entry.message.lower():
            return False
        return True
