from fastapi import APIRouter, Query
from app.models.user import UserCreateRequest, UserUpdateRequest, UserAssignRequest
from app.models.project import ProjectCreateRequest
from app.models.task import TaskCreateRequest
from app.models.project_member import ProjectMember
from app.controllers.manager_controller import (
    update_user,
    create_project,
    enum_projects,
    delete_member,
    project_details,
    assign_task,
    count_completed_tasks,
    count_in_progress_tasks,
    count_todo_tasks,
    create_member,
    create_task,
    get_busy_members,
    get_free_members
)

router = APIRouter()

# Endpoint to update data for an existing user
@router.put("/users")
async def update_user_data(user_request: UserUpdateRequest):
    return await update_user(user_request)

# Endpoint to create a project
@router.post("/projects")
async def create_new_project(project_request: ProjectCreateRequest):
    return await create_project(project_request)

# Endpoint to list all the projects of a manager
@router.get("/projects")
async def list_projects(manager_id: int):
    return await enum_projects(manager_id)

# Endpoint to remove member
@router.delete("/members/{member_id}")
async def remove_member(manager_id: int, member_id: int):
    result = await delete_member(manager_id, member_id)
    return result

# Endpoint to view details of a specific project
@router.get("/projects/{project_id}")
async def view_project_details(project_id: int, manager_id: int):
    return await project_details(project_id, manager_id)

# Endpoint to designate a task
@router.post("/tasks/{task_id}")
async def designate_task(task_id: int, assigned_to: int):
    result = await assign_task(task_id, assigned_to)
    return {"message": result}

# Endpoint to count completed tasks by priority in a project
@router.get("/projects/{project_id}/finished-tasks")
async def count_finished_tasks(project_id: int, manager_id: int):
    result = await count_completed_tasks(manager_id, project_id)
    return result

# Endpoint to count tasks in progress by priority in a project
@router.get("/projects/{project_id}/in-progress-tasks")
async def count_in_process_tasks(project_id: int, manager_id: int):
    result = await count_in_progress_tasks(manager_id, project_id)
    return result

# Endpoint to count pending tasks by priority in a project
@router.get("/projects/{project_id}/todo-tasks")
async def count_pending_tasks(project_id: int, manager_id: int):
    result = await count_todo_tasks(manager_id, project_id)
    return result

# Endpoint to create a new member
@router.post("/members")
async def create_new_member(manager_id: int, projectmember_request: ProjectMember):
    return await create_member(manager_id, projectmember_request)

# Endpoint to create a task
@router.post("/tasks")
async def create_new_task(task_request: TaskCreateRequest, manager_id: int = Query(...)):
    return await create_task(task_request, manager_id)

# Endpoint to get busy members
@router.get("/busy-members")
async def busy_members():
    return await get_busy_members()

# Endpoint to get members free from tasks
@router.get("/free-members")
async def free_members():
    return await get_free_members()
