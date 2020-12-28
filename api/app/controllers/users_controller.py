from fastapi import APIRouter
from .requests.user_request import RegisterUserRequest
from service.user_service import UserService

router = APIRouter()
user_service = UserService()

@router.post("/register_user", tags = ['register_user'])
async def register_user(request: RegisterUserRequest):
  return {'test':'test'}