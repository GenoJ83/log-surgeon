from concurrent.futures import ThreadPoolExecutor
from typing import List, Callable

def run_in_parallel(worker_fn: Callable, items: List, max_workers: int = 4):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        return list(executor.map(worker_fn, items))
