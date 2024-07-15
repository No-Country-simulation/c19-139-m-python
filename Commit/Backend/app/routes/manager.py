from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.models.user import UserCreateRequest, UserUpdateRequest
from app.controllers.manager_controller import (
    create_user,
    update_user
)

router = APIRouter()

# Endpoint to create a new user
@router.post("/users")
async def route_create_user(user_request: UserCreateRequest):
    return await create_user(user_request)

# Endpoint to update data for an existing user
@router.put("/users")
async def route_update_user_data(user_request: UserUpdateRequest):
    return update_user(user_request)

