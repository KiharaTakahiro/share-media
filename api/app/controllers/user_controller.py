from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services import user_service
from .base_controller import get_db
from app.schemas.user_schema import UserCreate, UserLogin

router = APIRouter()

@router.post("/users/create", tags = ['user_create'])
async def users_create(user: UserCreate, db: Session = Depends(get_db)):
  aleady_user = user_service.get_user_by_user_name(db, user.username)
  if aleady_user is not None:
    raise HTTPException(status_code=400, detail="登録済みのユーザがいます")
  user_service.create_user(db, user)
  return {'result':'success'}

@router.post("/users/login", tags = ["user_login"])
async def authenticate(user: UserLogin, db: Session = Depends(get_db)):
  login_user = user_service.get_user_by_user_login(db, user)
  if login_user is None:
    raise HTTPException(status_code=401, detail="ユーザが見つかりません")
  return {'result':'success'}
