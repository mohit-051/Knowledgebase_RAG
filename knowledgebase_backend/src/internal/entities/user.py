from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    user_id: Optional[str] = None
    username: Optional[str] = None


class UserBase(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None


class UserDetails(BaseModel):
    user_id: Optional[str] = None
    username: Optional[str] = None
