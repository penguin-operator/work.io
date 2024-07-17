import sqlite3
from typing import Self
from .user import User
from .work import Work
from .response import Response

class Database(object):
    __instance__: Self | None = None

    def __new__(cls) -> Self:
        if cls.__instance__ is None:
            cls.__instance__ = object.__new__(cls)
        return cls.__instance__

    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.curs = self.conn.cursor()

        self.curs.execute('''CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            description TEXT,
            role TEXT
        );''')
        self.curs.execute('''CREATE TABLE works (
            id INTEGER PRIMARY KEY,
            orderer INTEGER,
            name TEXT,
            description TEXT,
            status TEXT
        );''')
        self.curs.execute('''CREATE TABLE responses (
            id INTEGER PRIMARY KEY,
            orderer INTEGER,
            worker INTEGER,
            work INTEGER,
            content TEXT
        );''')
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def add_user(self, username: str, password: str, description: str = "", role: str = "orderer"):
        self.curs.execute(
            "INSERT INTO users(username, password, description, role) VALUES (?, ?, ?, ?)",
            (username, password, description, role),
        )
        self.conn.commit()

    def get_user(self, username: str) -> User | None:
        self.curs.execute(
            "SELECT username, password, description, role FROM users WHERE username=?",
            (username,),
        )
        if user := self.curs.fetchone():
            return User(
                username=user[0],
                password=user[1],
                description=user[2],
                role=user[3],
            )
