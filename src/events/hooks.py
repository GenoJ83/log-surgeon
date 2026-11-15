from typing import Callable, List

class EventHook:
    def __init__(self):
        self._subscribers: List[Callable] = []

    def subscribe(self, callback: Callable):
        self._subscribers.append(callback)

    def trigger(self, *args, **kwargs):
        for cb in self._subscribers:
            cb(*args, **kwargs)
