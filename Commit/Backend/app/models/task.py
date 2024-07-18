from pydantic import BaseModel
from typing import Optional
from datetime import date
from enum import Enum

class TaskStatusEnum(str, Enum):
    to_do = 'to do'
    in_progress = 'in progress'
    completed = 'completed'

class TaskPriorityEnum(str, Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'

class Task(BaseModel):
    task_id: Optional[int]
    project_id: int
    assigned_to: int
    title: str
    description: Optional[str]
    status: TaskStatusEnum
    priority: TaskPriorityEnum
    start_date: Optional[str]
    due_date: Optional[str]
    created_at: Optional[str]

class TaskCreateRequest(BaseModel):
    project_id: int
    assigned_to: int
    title: str
    description: Optional[str] = None
    status: Optional[str] = 'to do'
    priority: Optional[str] = 'medium'
    due_date: Optional[date] = None
