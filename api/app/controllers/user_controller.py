from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.common.exception import ValidationException
from app.services import user_service
from .base_controller import get_db
from app.schemas.user_schema import UserCreate, UserLogin, SessionUser
from app.schemas.token_schema import Token
from app.logger import logger

router = APIRouter()

@router.post("/users/create", tags = ['user_create'])
async def users_create(user: UserCreate, db: Session = Depends(get_db)):

  logger.debug(f'user: {user}')
  logger.debug(f'db: {db}')

  aleady_user = user_service.get_user_by_user_name(db, user.username)
  logger.debug(f'aleady_user: {aleady_user}')

  if aleady_user is not None:
    logger.warn(f'aleady_user: {aleady_user}')
    raise ValidationException("登録済みのユーザがいます")

  user_service.create_user(db, user)
  return {'result':'success'}

@router.post("/users/login", tags = ["user_login"], response_model=Token)
async def authenticate(user: UserLogin, db: Session = Depends(get_db)):
  
  logger.debug(f'user: {user}')
  logger.debug(f'db: {db}')

  login_user = user_service.get_user_by_user_login(db, user)
  logger.debug(f'login_user: {login_user}')

  if login_user is None:
    logger.warn(f'user: {user}')
    raise ValidationException("ユーザが見つかりません")
    
  tokens = user_service.create_token(db, login_user.id)
  logger.debug(f'tokens: {tokens}')

  return {'access_token': tokens['access_token'], 'refresh_token': tokens['refresh_token']}

@router.post("/users/refresh_token", tags=["user_refresh_token"], response_model=Token)
async def refresh_token(current_user: SessionUser = Depends(user_service.get_current_user_with_refresh_token)):
  logger.debug(f'current_user: {current_user}')
  tokens = create_tokens(current_user.id)
  logger.debug(f'tokens: {tokens}')
  return tokens

# TODO: テスト用に追加するだけで実際には削除する
@router.get("/users/me/")
async def read_users_me(current_user = Depends(user_service.get_current_user)):
  logger.debug(current_user)
  return current_user