from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.common.exception import ValidationException
from app.services import user_service
from .base_controller import get_db
from app.schemas.user_schema import UserCreate, UserLogin, SessionUser
from app.schemas.token_schema import Token

router = APIRouter()

@router.post("/users/create", tags = ['user_create'])
async def users_create(user: UserCreate, db: Session = Depends(get_db)):

  # 既に存在するユーザの場合はエラーで返却する
  aleady_user = user_service.get_user_by_user_name(db, user.username)
  if aleady_user is not None:
    raise ValidationException("登録済みのユーザがいます")

  user_service.create_user(db, user)
  return {'result':'success'}

@router.post("/users/login", tags = ["user_login"], response_model=Token)
async def authenticate(user: UserLogin, db: Session = Depends(get_db)):
  # ユーザが存在するかを確認して存在しない場合はエラーで返却する
  login_user = user_service.get_user_by_user_login(db, user)
  if login_user is None:
    raise ValidationException("ユーザが見つかりません")
    
  # トークンを生成する
  tokens = user_service.create_token(db, login_user.id)
  return {'access_token': tokens['access_token'], 'refresh_token': tokens['refresh_token'], 'token_type': 'bearer'}

@router.post("/users/refresh_token", tags=["user_refresh_token"], response_model=Token)
async def refresh_token(current_user: SessionUser = Depends(user_service.get_current_user_with_refresh_token)):
  """リフレッシュトークンでトークンを再取得"""
  return create_tokens(current_user.id)

# TODO: テスト用に追加するだけで実際には削除する
@router.get("/users/me/", response_model=SessionUser)
async def read_users_me(current_user: SessionUser = Depends(user_service.get_current_user)):
  """ログイン中のユーザーを取得"""
  return current_user