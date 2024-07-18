from app.config.db_conexion import data_conexion
from app.models.user import User, UserCreateRequest, UserUpdateRequest, UserAssignRequest
from app.models.project import ProjectCreateRequest, Project

async def create_user(user_request: UserCreateRequest):
    params = [
        user_request.name,
        user_request.email,
        user_request.password
    ]
    result = data_conexion.execute_procedure('sp_create_user', params)
    return result

async def update_user(user_request: UserUpdateRequest):
    params = [
        user_request.user_id,
        user_request.email,
        user_request.password
    ]
    result = data_conexion.execute_procedure('sp_update_user_credentials', params)
    return result

async def assign_member_to_project(manager_id: int, project_id: int, member_email: str, role: str, seniority: str):
    params = [
        manager_id,
        project_id,
        member_email,
        role,
        seniority
    ]
    result = data_conexion.execute_procedure('sp_assign_member_to_project', params)
    return result

async def create_project(user_request: ProjectCreateRequest):
    params = [
        user_request.manager_id,
        user_request.name,
        user_request.description,
        user_request.start_date,
        user_request.due_date,
        user_request.status
    ]
    result = data_conexion.execute_procedure('sp_create_project', params)
    return result

async def list_projects(manager_id: int):
    params = [manager_id]
    result = data_conexion.execute_procedure('sp_list_manager_projects', params)
    return result

async def delete_member(user_id: int):
    params = [user_id]
    result = data_conexion.execute_procedure('sp_delete_member', params)
    return result

async def project_details(project_id: int, manager_id: int):
    params = [project_id, manager_id]
    result = data_conexion.execute_procedure('sp_view_project_details', params)
    return result
