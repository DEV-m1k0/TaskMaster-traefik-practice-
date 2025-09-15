from models import User
from database import SessionLocal, Base, engine

async def init_db():
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as session:
        if not session.query(User).first():
            admin = User(username="admin", password="admin", first_name="John", last_name="Doe", role="admin")
            user = User(username="user", password="user", first_name="Jane", last_name="Miller", role="user")
            
            session.add_all([admin, user])
            session.commit()


async def destroy_db():
    Base.metadata.drop_all(bind=engine)