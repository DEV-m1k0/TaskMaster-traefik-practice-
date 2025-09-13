from models import User
from database import SessionLocal
from schemas.user import UserBase


async def check_credentials(username: str, password: str) -> bool:
    with SessionLocal() as session:
        user = session.query(User).where(User.username==username).first()
        if user and user.password == password:
            return True
        return False