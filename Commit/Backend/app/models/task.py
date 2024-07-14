from pydantic import BaseModel
from typing import Optional
from datetime import date

class Task(BaseModel):
    task_id: Optional[int]
    project_id: int
    assigned_to: int
    title: str
    description: Optional[str]
    status: str
    priority: str
    due_date: Optional[date]
    created_at: Optional[str]

class TaskCreateRequest(BaseModel):
    project_id: int
    assigned_to: int
    title: str
    description: Optional[str] = None
    status: Optional[str] = 'to do'
    priority: Optional[str] = 'medium'
    due_date: Optional[date] = None
