from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from enum import Enum

class ProjectStatusEnum(str, Enum):
    not_started = 'not started'
    in_progress = 'in progress'
    completed = 'completed'

class Project(BaseModel):
    project_id: Optional[int]
    manager_id: int
    name: str
    description: Optional[str]
    start_date: Optional[date]
    due_date: Optional[date]
    status: ProjectStatusEnum = ProjectStatusEnum.not_started
    created_at: Optional[str]

class ProjectCreateRequest(BaseModel):
    manager_id: int
    name: str
    description: Optional[str] = None
    start_date: Optional[date] = None
    due_date: Optional[date] = None
    status: Optional[ProjectStatusEnum] = ProjectStatusEnum.not_started 
