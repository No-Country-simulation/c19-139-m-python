from app.config.db_conexion import data_conexion
from app.models.user import User, UserCreateRequest, UserUpdateRequest, UserAssignRequest, SeniorityEnum
from app.models.project import ProjectCreateRequest, Project
from app.models.task import TaskCreateRequest
 

async def update_user(user_request: UserUpdateRequest):
    params = [
        user_request.user_id,
        user_request.email,
        user_request.password
    ]
    result = await data_conexion.execute_procedure('sp_update_user_credentials', params)
    return result

async def create_project(project_request: ProjectCreateRequest):
    params = [
        project_request.manager_id,
        project_request.name,
        project_request.description,
        project_request.start_date,
        project_request.due_date
    ]
    result = await data_conexion.execute_procedure('sp_create_project', params)
    return result

async def assign_member_to_project(manager_id: int, project_id: int, member_email: str, role: str, seniority: SeniorityEnum):
    params = [
        manager_id,
        project_id,
        member_email,
        role,
        seniority.value
    ]
    result = await data_conexion.execute_procedure('sp_assign_member_to_project', params)
    return result

async def list_projects(manager_id: int):
    params = [manager_id]
    result = await data_conexion.execute_procedure('sp_list_manager_projects', params)
    return result

async def delete_member(user_id: int):
    params = [user_id]
    result = await data_conexion.execute_procedure('sp_delete_member', params)
    return result

async def project_details(project_id: int, manager_id: int):
    params = [project_id, manager_id]
    result = await data_conexion.execute_procedure('sp_view_project_details', params)
    return result

async def assign_task(task_id: int, assigned_to: int):
    params = [
        task_id,
        assigned_to
    ]
    result = await data_conexion.execute_procedure('sp_assign_task', params)
    return result

async def count_completed_tasks(manager_id: int, project_id: int):
    params = [
        manager_id,
        project_id
    ]
    result = await data_conexion.execute_procedure('sp_count_completed_tasks', params)
    return result

async def count_in_progress_tasks(manager_id: int, project_id: int):
    params = [
        manager_id,
        project_id
    ]
    result = await data_conexion.execute_procedure('sp_count_in_progress_tasks', params)
    return result

async def count_todo_tasks(manager_id: int, project_id: int):
    params = [
        manager_id,
        project_id
    ]
    result = await data_conexion.execute_procedure('sp_count_todo_tasks', params)
    return result

async def create_member(manager_id: int, member_request: UserCreateRequest):
    params = [
        manager_id,
        member_request.name,
        member_request.email,
        member_request.password
    ]
    result = await data_conexion.execute_procedure('sp_create_member', params)
    return result

async def create_task(task_request: TaskCreateRequest, manager_id):
    params = [
        manager_id,
        task_request.project_id,
        task_request.title,
        task_request.description,
        task_request.assigned_to,
        task_request.status,
        task_request.priority,
        task_request.start_date,
        task_request.due_date
    ]
    result = await data_conexion.execute_procedure('sp_create_task', params)
    return result

async def get_busy_members():
    result = await data_conexion.execute_procedure('sp_get_busy_members')
    return result

async def get_free_members():
    result = await data_conexion.execute_procedure('sp_get_free_members')
    return result
