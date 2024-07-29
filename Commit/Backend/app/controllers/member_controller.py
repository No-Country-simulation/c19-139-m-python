from fastapi import APIRouter
from app.config.db_conexion import data_conexion
from app.models.task import EditTaskRequest

router = APIRouter()


async def edit_task(task_id: int, request: EditTaskRequest):
    params = [task_id, request.assigned_member_id, request.status.value]
    print(f"Parameters: {params}")
    result = data_conexion.execute_procedure("sp_edit_task", params)

    tables = [
        "Users",
        "Projects",
        "Project_Members",
        "Tasks",
        "Documents",
        "Reports",
        "Comments",
        "Messages",
        "Notifications",
    ]
    data_conexion.export_to_excel(tables)

    return result
