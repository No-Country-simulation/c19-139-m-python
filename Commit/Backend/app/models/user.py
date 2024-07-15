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

class UserAssignRequest(BaseModel):
    manager_id: int
    project_id: int
    member_name: str
    member_email: EmailStr
    member_password: str

class UsersLoginRequest(BaseModel):
    email: EmailStr
    password_hash: str
