from pydantic import BaseModel
from typing import Optional

class Comment(BaseModel):
    comment_id: Optional[int]
    user_id: int
    task_id: Optional[int]
    project_id: Optional[int]
    content: str
    created_at: Optional[str]
