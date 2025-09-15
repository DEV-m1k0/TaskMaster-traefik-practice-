from sqlalchemy import Integer, String, Column, DateTime
from database import Base

import bcrypt
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    role = Column(String, nullable=False)

    def __init__(self, username, password, first_name, last_name, role):
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.first_name = first_name
        self.last_name = last_name
        self.role = role

    def __repr__(self):
        return f"<User(username={self.username})>"
    

    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    

class RefreshToken(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, index=True)
    refresh_token = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)
    expire = Column(DateTime, nullable=False)

    def __init__(self, refresh_token: str, user_id: int, expire: datetime):
        self.refresh_token = refresh_token
        self.user_id = user_id
        self.expire = expire


    def __repr__(self):
        return f"<Token(refresh_token={self.refresh_token})>"
    

    def verify_token(self, refresh_token: str):
        return self.refresh_token == refresh_token
    

    def is_expired(self):
        return datetime.now() > self.expire