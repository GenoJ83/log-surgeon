from functools import lru_cache
import re

@lru_cache(maxsize=128)
def get_compiled_regex(pattern: str):
    return re.compile(pattern)
