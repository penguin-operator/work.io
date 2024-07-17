from pydantic import BaseModel

class Work(BaseModel):
    orderer: int
    name: str
    description: str
    status: str
