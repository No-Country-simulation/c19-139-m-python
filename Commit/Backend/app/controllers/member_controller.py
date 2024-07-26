from fastapi import APIRouter
from app.config.db_conexion import data_conexion
from app.models.task import EditTaskRequest

router = APIRouter()

async def edit_task(task_id: int, request: EditTaskRequest):
   params = [
      task_id,
      request.assigned_member_id,
      request.status.value
   ]
   print(f"Parameters: {params}")
   result = await data_conexion.execute_procedure('sp_edit_task', params)
   return result

