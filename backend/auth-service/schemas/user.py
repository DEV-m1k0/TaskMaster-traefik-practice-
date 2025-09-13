from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str


class UserLogin(UserBase):
    pass


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    username: str | None = None
    password: str | None = None


class UserGet(BaseModel):
    id: int


class UserDelete(BaseModel):
    id: int