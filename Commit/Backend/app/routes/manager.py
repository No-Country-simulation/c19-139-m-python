from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.models.user import UserCreateRequest, UserUpdateRequest, UserAssignRequest
from app.models.project import ProjectCreateRequest
from app.controllers.manager_controller import (
    create_user,
    update_user,
    assign_member_to_project,
    create_project,
    list_projects,
    delete_member,
    project_details,
    assign_task,
    count_completed_tasks,
    count_in_progress_tasks
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
    manager_id = user_request.manager_id
    member_email = user_request.member_email
    role = user_request.role
    seniority = user_request.seniority

    result = await assign_member_to_project(manager_id, project_id, member_email, role, seniority)
    return {"message": result}

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

# Endpoint to view details of a specific project
@router.get("/projects/{project_id}")
async def view_project_details(project_id: int, manager_id: int):
    return await project_details(project_id, manager_id)

# Endpoint to assign a task
@router.post("/tasks/{task_id}/assign")
async def route_assign_task(task_id: int, assigned_to: int):
    result = await assign_task(task_id, assigned_to)
    return {"message": result}

# Endpoint to count completed tasks by priority in a project
@router.get("/projects/{project_id}/completed-tasks")
async def route_count_completed_tasks(project_id: int, manager_id: int):
    result = await count_completed_tasks(manager_id, project_id)
    return result

# Endpoint to count tasks in progress by priority in a project
@router.get("/projects/{project_id}/in-progress-tasks")
async def route_count_in_progress_tasks(project_id: int, manager_id: int):
    result = await count_in_progress_tasks(manager_id, project_id)
    return result