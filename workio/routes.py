from fastapi import FastAPI, Request
from database import Database, User, Work, Response

app = FastAPI()
db = Database()

@app.post('/user')
async def add_user(user: User) -> dict[str, str | User]:
    if db.get_user(user.username):
        return { "status": "error", "message": "User already exists", }
    db.add_user(user.username, user.password, user.description or "", user.role or "orderer")
    return { "status": "ok", "user": user, }

@app.get('/user')
async def get_user(username: str) -> dict[str, str | User]:
    user = db.get_user(username)
    if not user:
        return { "status": "error", "message": "User does not exist", }
    return { "status": "ok", "user": user, }
