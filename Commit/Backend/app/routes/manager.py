from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.models.user import UserCreateRequest, UserUpdateRequest, UserAssignRequest
from app.models.project import ProjectCreateRequest
from app.controllers.manager_controller import (
    create_user,
    update_user,
    assign_member,
    create_project,
    list_projects,
    delete_member
)

router = APIRouter()

# Endpoint to create a new user
@router.post("/users")
async def route_create_user(user_request: UserCreateRequest):
    return await create_user(user_request)

# Endpoint to update data for an existing user
@router.put("/users")
async def route_update_user_data(user_request: UserUpdateRequest):
    return await update_user(user_request)

# Enpoint to assign a member to a project
@router.post("/projects/{project_id}/members")
async def route_assign_member_to_project(project_id: int, user_request: UserAssignRequest):
    return await assign_member(project_id, user_request)

# Endpoint to create a project
@router.post("/projects")
async def route_create_new_project(user_request: ProjectCreateRequest):
    return await create_project(user_request)

# Endpoint to list all the projects of a manager
@router.get("/projects")
async def route_list_manager_projects(manager_id: int):
    return await list_projects(manager_id)

# Endpoint to list all the projects of a manager
@router.delete("/members/{user_id}")
async def route_delete_member_from_project(user_id: int):
    return await delete_member(user_id)
