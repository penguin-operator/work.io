from typing import Literal
from pydantic import BaseModel

class Work(BaseModel):
    orderer: int
    name: str
    description: str
    status: Literal["new", "in-progress", "done"]
