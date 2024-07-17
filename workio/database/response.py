from pydantic import BaseModel

class Response(BaseModel):
    orderer: int
    worker: int
    work: int
    content: str
