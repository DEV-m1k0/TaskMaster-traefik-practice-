import jwt
from jwt.exceptions import InvalidTokenError
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException

from models import User
from database import SessionLocal
from jwt_config import ACCESS_SECRET_KEY, ALGORITHM


security = HTTPBearer()


async def check_credentials(username: str, password: str) -> bool:
    with SessionLocal() as session:
        user = session.query(User).where(User.username==username).first()
        if user and user.verify_password(password):
            return True
        return False


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, key=ACCESS_SECRET_KEY, algorithms=[ALGORITHM])
        if payload['type'] != 'access':
            raise HTTPException(status_code=401, detail="Invalid token")
        
        username: str = payload['sub']
        if not username:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")