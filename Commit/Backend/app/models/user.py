from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum


class RoleEnum(str, Enum):
    support = "support"
    manager = "manager"
    member = "member"


class SeniorityEnum(str, Enum):
    trainee = "trainee"
    junior = "junior"
    senior = "senior"


class User(BaseModel):
    user_id: Optional[int]
    name: str
    email: EmailStr
    password_hash: str
    role: RoleEnum
    created_at: Optional[str]


class UserCreateRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserUpdateRequest(BaseModel):
    email: Optional[EmailStr] = None
    new_email: Optional[EmailStr] = None
    new_password: Optional[str] = None


class UserAssignRequest(BaseModel):
    manager_id: int
    project_id: int
    member_name: str
    member_email: EmailStr
    member_password: str
    role: str
    seniority: SeniorityEnum


class UsersLoginRequest(BaseModel):
    email: EmailStr
    password_hash: str
