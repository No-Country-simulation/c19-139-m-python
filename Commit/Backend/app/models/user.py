from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    user_id: Optional[int]
    name: str
    email: EmailStr
    password_hash: str
    role: str
    created_at: Optional[str]

class UserCreateRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserUpdateRequest(BaseModel):
    user_id: int
    email: Optional[EmailStr] = None
    password: Optional[str] = None
