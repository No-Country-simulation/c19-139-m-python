from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum


class SeniorityEnum(str, Enum):
    trainee = "trainee"
    junior = "junior"
    senior = "senior"


class AvailabilityEnum(str, Enum):
    free = "free"
    busy = "busy"


class ProjectMember(BaseModel):
    project_id: int
    member_name: str
    member_email: EmailStr
    member_password: str
    role: str
    seniority: SeniorityEnum
    availability: AvailabilityEnum
