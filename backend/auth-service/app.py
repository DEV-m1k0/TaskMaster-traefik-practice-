from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from schemas.user import UserLogin

from logic.db import init_db, destroy_db
from logic.login import check_credentials


app = FastAPI()

allow_origins = ["*", "http://localhost", "http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/login")
async def login(user: UserLogin):
    if not user.username or not user.password:
        raise HTTPException(status_code=400, detail="Username and password are required")
    if await check_credentials(user.username, user.password):
        return {
                "username": user.username,
                "password": user.password,
                "message": "Login successful"
            }
    return {
        "error": "user not found"
    }


@app.on_event("startup")
async def startup_event():
    # await destroy_db()
    await init_db()