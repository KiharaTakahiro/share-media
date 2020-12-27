from fastapi import APIRouter
from .requests.user_request import RegisterUserRequest

router = APIRouter()

@router.post("/register_user", tags = ['register_user'])
async def register_user(request: RegisterUserRequest):
  return {"test" : "test"}
