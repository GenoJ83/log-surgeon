from typing import List, Generator
from src.models.entry import LogEntry

def chunk_stream(lines: Generator[str, None, None], chunk_size: int = 1000) -> Generator[List[str], None, None]:
    chunk = []
    for line in lines:
        chunk.append(line)
        if len(chunk) >= chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk
