from pydantic import BaseModel
from typing import Optional


class Document(BaseModel):
    document_id: Optional[int]
    project_id: int
    uploaded_by: int
    title: str
    file_path: str
    created_at: Optional[str]
