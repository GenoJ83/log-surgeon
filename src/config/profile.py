import json
import os

def load_profile(path: str):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}
