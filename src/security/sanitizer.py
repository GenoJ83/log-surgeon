import os

def sanitize_path(base_dir: str, target_path: str) -> str:
    resolved = os.path.abspath(os.path.join(base_dir, target_path))
    if not resolved.startswith(os.path.abspath(base_dir)):
        raise ValueError('Directory traversal detected')
    return resolved
