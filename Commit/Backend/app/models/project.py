from pydantic import BaseModel
from typing import Optional
from datetime import date

class Project(BaseModel):
    project_id: Optional[int]
    manager_id: int
    name: str
    description: Optional[str]
    start_date: Optional[date]
    due_date: Optional[date]
    status: str
    created_at: Optional[str]

class ProjectCreateRequest(BaseModel):
    manager_id: int
    name: str
    description: Optional[str] = None
    start_date: Optional[date] = None
    due_date: Optional[date] = None
    status: Optional[str] = 'not started'
