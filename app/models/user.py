from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    first_name: str
    last_name: str
    age: float
    profession : Optional[str] = None
