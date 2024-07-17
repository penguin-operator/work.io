from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    description: Optional[str] = None
    role: Optional[str] = None
