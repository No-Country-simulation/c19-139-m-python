from pydantic import BaseModel
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
    user_id: int
    project_id: int
    role: str
    seniority: SeniorityEnum
    availability: AvailabilityEnum
    created_at: Optional[str]
