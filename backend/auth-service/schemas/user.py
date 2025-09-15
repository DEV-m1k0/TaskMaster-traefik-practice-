from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    role: str


class User(UserBase):
    id: int

class UserLogin(BaseModel):
    username: str
    password: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    username: str | None = None
    password: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    role: str | None = None


class UserGet(BaseModel):
    id: int


class UserDelete(BaseModel):
    id: int