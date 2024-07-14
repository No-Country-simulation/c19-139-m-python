from pydantic import BaseModel
from typing import Optional

class Report(BaseModel):
    report_id: Optional[int]
    project_id: int
    generated_by: int
    content: str
    created_at: Optional[str]
