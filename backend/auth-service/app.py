from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from schemas.user import UserLogin

from logic.db import init_db, destroy_db
from logic.login import check_credentials, get_current_user
from logic.account import get_account_by_username
from logic.token import save_refresh_token_for_user, create_refresh_token, create_access_token


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
    if not await check_credentials(user.username, user.password):
        raise HTTPException(status_code=404, detail="Invalid credentials")

    access_token = create_access_token({"sub": user.username})
    refresh_token = create_refresh_token({"sub": user.username})

    await save_refresh_token_for_user(user.username, refresh_token)

    #TODO: send refresh token to client as cookie
    
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@app.get("/account")
async def account(current_user: str = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    user = await get_account_by_username(current_user)
    return {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name
        }


@app.on_event("startup")
async def startup_event():
    await destroy_db()
    await init_db()