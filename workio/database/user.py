from typing import Literal
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    description: str | None = None
    role: Literal['orderer', 'worker']
