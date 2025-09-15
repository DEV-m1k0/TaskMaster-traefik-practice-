from models import RefreshToken
from database import SessionLocal
from jwt_config import ACCESS_TOKEN_EXPIRE_MINUTES, ACCESS_SECRET_KEY, ALGORITHM, REFRESH_SECRET_KEY, REFRESH_TOKEN_EXPIRE_MINUTES

from logic.account import get_account_by_username

from datetime import datetime, timedelta
import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import HTTPException


async def save_refresh_token_for_user(username: str, refresh_token: str):
    with SessionLocal() as session:
        user = await get_account_by_username(username)
        
        user_refresh_token = session.query(RefreshToken).where(RefreshToken.user_id==user.id).first()

        if user_refresh_token:
            user_refresh_token.refresh_token = refresh_token
            user_refresh_token.expire = datetime.now() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
        else:
            session.add(RefreshToken(refresh_token, user.id, datetime.now() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)))
        session.commit()


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "type": "access"})
    return jwt.encode(to_encode, key=ACCESS_SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, key=ACCESS_SECRET_KEY, algorithm=ALGORITHM)


def validate_refresh_token(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, key=REFRESH_SECRET_KEY, algorithms=[ALGORITHM])
        if payload['type'] != 'refresh':
            raise HTTPException(status_code=401, detail="Invalid token")
        
        username: str = payload['sub']
        if not username:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        if not RefreshToken.verify_token(refresh_token):
            raise HTTPException(status_code=401, detail="Invalid token")
        
        if RefreshToken.is_expired(refresh_token):
            raise HTTPException(status_code=401, detail="Token expired")

        return username

    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")