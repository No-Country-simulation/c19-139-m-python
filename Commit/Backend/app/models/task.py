from pydantic import BaseModel
from typing import Optional
from datetime import date
from enum import Enum


class TaskStatusEnum(str, Enum):
    to_do = "to do"
    in_progress = "in progress"
    completed = "completed"


class TaskPriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Task(BaseModel):
    task_id: Optional[int]
    project_id: int
    assigned_member_id: int
    title: str
    description: Optional[str]
    status: TaskStatusEnum
    priority: TaskPriorityEnum
    start_date: Optional[date]
    due_date: Optional[date]
    created_at: Optional[date]


class TaskCreateRequest(BaseModel):
    project_id: int
    assigned_member_id: Optional[int] = None
    title: str
    description: Optional[str] = None
    status: TaskStatusEnum
    priority: TaskPriorityEnum
    start_date: Optional[date]
    due_date: Optional[date]


class EditTaskRequest(BaseModel):
    assigned_member_id: int
    status: TaskStatusEnum
