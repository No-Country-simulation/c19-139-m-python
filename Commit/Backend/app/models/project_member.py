from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum

class SeniorityEnum(str, Enum):
    trainee = 'trainee'
    junior = 'junior'
    senior = 'senior'

class AvailabilityEnum(str, Enum):
    free = 'free'
    busy = 'busy'

class ProjectMember(BaseModel):
    member_id: Optional[int]
    project_id: int
    role: str
    seniority: SeniorityEnum
    availability: AvailabilityEnum
    member_email: EmailStr
    member_name: str
    member_password: str
    created_at: Optional[str]
