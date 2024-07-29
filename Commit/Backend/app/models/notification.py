from pydantic import BaseModel
from typing import Optional


class Notification(BaseModel):
    notification_id: Optional[int]
    user_id: int
    content: str
    is_read: Optional[bool] = False
    created_at: Optional[str]
