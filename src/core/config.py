from pydantic import BaseModel

class Config(BaseModel):
    date_format: str = '%Y-%m-%d %H:%M:%S'
    buffer_size: int = 10000
    max_error_rate: float = 0.05
