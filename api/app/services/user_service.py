from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session
from app.common.exception import TokenException
from app.models import User
from app.schemas.user_schema import UserCreate, UserLogin
from app.common.convert import convert_hash
from datetime import datetime, timedelta
from jose import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# TODO: 実際の値はconfigから取得するように変更する
HASH_SOLT = "SREMEHADIASTOL"
TOKEN_SECRETE_KEY = "REMHAKOADISSEENTTOL"

def create_user(db: Session, user: UserCreate):
    hashed_password = convert_hash(user.password + HASH_SOLT)
    db_user = User(username=user.username, email=user.email, password=hashed_password, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_user_name(db: Session, username: str):
    return db.query(User).filter(User.username==username).first()

def get_user_by_user_id(db: Session, id: int):
    return db.query(User).filter(User.id==id).first()

def get_user_by_user_login(db: Session, user: UserLogin):
    hashed_password = convert_hash(user.password + HASH_SOLT)
    return db.query(User).filter(User.username==user.username, User.password==hashed_password).first()

def create_token(db: Session, user_id: int):
  
  # ペイロード作成
  # TODO: 期間もconfigから取得するように変更する
  access_payload = {
      'token_type': 'access_token',
      'exp': datetime.utcnow() + timedelta(minutes=60),
      'user_id': user_id,
  }
  refresh_payload = {
      'token_type': 'refresh_token',
      'exp': datetime.utcnow() + timedelta(days=90),
      'user_id': user_id,
  }

  # トークン作成
  # TODO: algorithmもconfigに配置する
  access_token = jwt.encode(access_payload, TOKEN_SECRETE_KEY, algorithm='HS256')
  refresh_token = jwt.encode(refresh_payload, TOKEN_SECRETE_KEY, algorithm='HS256')
  
  # リフレッシュトークンを更新する
  db_user = get_user_by_user_id(db, user_id)
  db_user.refresh_token = refresh_token
  db.commit()
  db.refresh(db_user)

  return {'access_token': access_token, 'refresh_token': refresh_token}

def get_current_user_from_token(token: str, token_type: str):
  """tokenからユーザーを取得"""
  # トークンをデコードしてペイロードを取得。有効期限と署名は自動で検証される。
  payload = jwt.decode(token, TOKEN_SECRETE_KEY, algorithms=['HS256'])

  # トークンタイプが一致することを確認
  if payload['token_type'] != token_type:
    raise TokenException('トークンタイプ不一致')

  # DBからユーザーを取得
  user = User.get_by_id(payload['user_id'])

  # リフレッシュトークンの場合、受け取ったものとDBに保存されているものが一致するか確認
  if token_type == 'refresh_token' and user.refresh_token != token:
    raise TokenException('リフレッシュトークン不一致')
  return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """アクセストークンからログイン中のユーザーを取得"""
    return get_current_user_from_token(token, 'access_token')

async def get_current_user_with_refresh_token(token: str = Depends(oauth2_scheme)):
    """リフレッシュトークンからログイン中のユーザーを取得"""
    return get_current_user_from_token(token, 'refresh_token')