import json
import os

class SessionManager:
    def __init__(self, path: str = '.logsurgeon_session.json'):
        self.path = path

    def save_state(self, data: dict):
        with open(self.path, 'w') as f:
            json.dump(data, f)

    def load_state(self) -> dict:
        if os.path.exists(self.path):
            with open(self.path) as f:
                return json.load(f)
        return {}
