from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.models.user import UserCreateRequest
from app.controllers.manager_controller import (
    create_user
)

router = APIRouter()

# Endpoint to create a new user
@router.post("/users")
async def route_create_user(user_request: UserCreateRequest):
    return await create_user(user_request)
