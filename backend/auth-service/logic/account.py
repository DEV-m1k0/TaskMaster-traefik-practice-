from models import User
from database import SessionLocal

async def get_account_by_username(username: str) -> User:
    with SessionLocal() as session:
        return session.query(User).where(User.username==username).first()
