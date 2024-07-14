from app.config.db_conexion import data_conexion
from app.models.user import UserCreateRequest, UserUpdateRequest, UserAssignRequest
from app.models.project import ProjectCreateRequest

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

async def assign_member(user_request: UserAssignRequest):
    params = [
        user_request.manager_id,
        user_request.project_id,
        user_request.member_name,
        user_request.member_email,
        user_request.member_password
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