from fastapi import APIRouter
from app.controllers.member_controller import edit_task
from app.models.task import EditTaskRequest

router = APIRouter()

@router.put("/tasks/edit/{task_id}")
async def update_task_status(task_id: int, request: EditTaskRequest):
    return await edit_task(task_id, request)
