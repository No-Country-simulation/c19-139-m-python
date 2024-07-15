from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.models.user import UserCreateRequest, UserUpdateRequest, UserAssignRequest
from app.models.project import ProjectCreateRequest, Project
from app.controllers.manager_controller import (
    create_user,
    update_user,
    assign_member,
    create_project,
    list_projects,
    delete_member,
    project_details
)

router = APIRouter()

# Endpoint to create a new user
@router.post("/users", response_model=dict, tags=["Users"])
async def create_new_user(user_request: UserCreateRequest):
    try:
        result = await create_user(user_request)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to update data for an existing user
@router.put("/users", response_model=dict, tags=["Users"])
async def update_user_data(user_request: UserUpdateRequest):
    try:
        result = await update_user(user_request)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Enpoint to assign a member to a project
@router.post("/projects/{project_id}/members", response_model=dict, tags=["Projects"])
async def assign_member_to_project(project_id: int, user_request: UserAssignRequest):
    try:
        # Validate that project_id in UserAssignRequest matches the path
        if user_request.project_id != project_id:
            raise HTTPException(status_code=400, detail="Project ID in request body must match the path parameter.")
        result = await assign_member(user_request)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to create a project
@router.post("/projects", response_model=dict, tags=["Projects"])
async def create_new_project(user_request: ProjectCreateRequest):
    try:
        result = await create_project(user_request)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to list all the projects of a manager
@router.get("/projects", response_model=dict, tags=["Projects"])
async def list_manager_projects(manager_id: int):
    try:
        result = await list_projects(manager_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to list all the projects of a manager
@router.delete("/members/{user_id}", response_model=dict, tags=["Members"])
async def delete_member_from_project(user_id: int):
    try:
        result = await delete_member(user_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to view details of a specific project
@router.get("/projects/{project_id}", response_model=dict, tags=["Projects"])
async def view_project_details(project_id: int, manager_id: int):
    try:
        result = await project_details(project_id, manager_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
