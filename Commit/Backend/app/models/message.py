from pydantic import BaseModel
from typing import Optional


class Message(BaseModel):
    message_id: Optional[int]
    sender_id: int
    receiver_id: int
    content: str
    created_at: Optional[str]
