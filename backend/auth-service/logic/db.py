from models import User
from database import SessionLocal, Base, engine
from sqlalchemy import MetaData

async def init_db():
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as session:
        if not session.query(User).first():
            user1 = User(username="user1", password="user1")
            user2 = User(username="user2", password="user2")
            
            session.add_all([user1, user2])
            session.commit()


async def destroy_db():
    Base.metadata.drop_all(bind=engine)