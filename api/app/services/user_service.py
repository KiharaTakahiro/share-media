from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from app.logger import logger
from sqlalchemy.orm import Session
from app.common.exception import TokenException
from app.models import User
from app.schemas.user_schema import UserCreate, UserLogin
from app.common.convert import convert_hash
from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.controllers.base_controller import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# TODO: 実際の値はconfigから取得するように変更する
HASH_SOLT = "SREMEHADIASTOL"
TOKEN_SECRETE_KEY = "REMHAKOADISSEENTTOL"

def create_user(db: Session, user: UserCreate) -> User:
  """ ユーザ作成処理

  Args:
      db (Session): dbのセッション情報
      user (UserCreate): 登録するユーザの情報

  Returns:
      User: 登録したユーザの情報
  """

  logger.debug(f'db: {db}')
  logger.debug(f'user: {user}')
  
  hashed_password = convert_hash(user.password + HASH_SOLT)
  logger.debug(f'hashed_password: {hashed_password}')

  db_user = User(username=user.username, email=user.email, password=hashed_password, age=user.age)
  logger.info(f'db_user: {db_user}')

  db.add(db_user)
  db.commit()
  db.refresh(db_user)

  return db_user

def get_user_by_user_name(db: Session, username: str):
  """ ユーザ名をもとにユーザテーブルを検索

  Args:
      db (Session): dbのセッション情報
      username (str): ユーザ名

  Returns:
      User: ユーザ情報
  """

  logger.debug(f'db: {db}')
  logger.debug(f'username: {username}')

  db_user = db.query(User).filter(User.username==username).first()
  logger.debug(f'db_user: {db_user}')
  
  return db_user

def get_user_by_user_id(db: Session, id: int):
  """ ユーザIDをもとにユーザを検索

  Args:
      db (Session): dbのセッション情報
      id (int): ユーザID

  Returns:
      User: ユーザ情報
  """

  logger.debug(f'db: {db}')
  logger.debug(f'id: {id}')

  db_user = db.query(User).filter(User.id==id).first()
  logger.debug(f'db_user: {db_user}')

  return db_user

def get_user_by_user_login(db: Session, user: UserLogin):
  """ ログイン情報によるユーザ情報取得処理

  Args:
      db (Session): dbの接続情報
      user (UserLogin): ログイン画面での入力情報

  Returns:
      User: ユーザ情報
  """

  logger.debug(f'db: {db}')
  logger.debug(f'user: {user}')

  hashed_password = convert_hash(user.password + HASH_SOLT)
  logger.debug(f'hashed_password: {hashed_password}')

  db_user = db.query(User).filter(User.username==user.username, User.password==hashed_password).first()
  logger.debug(f'db_user: {db_user}')
  
  return db_user

def create_token(db: Session, user_id: int):
  """ トークン作成

  Args:
      db (Session): dbの接続情報
      user_id (int): ユーザID

  Returns:
      dict: トークン
  """

  logger.debug(f'user_id: {user_id}')
  logger.debug(f'db: {db}')

  # TODO: 期間もconfigから取得するように変更する
  access_payload = {
      'token_type': 'access_token',
      'exp': datetime.utcnow() + timedelta(minutes=60),
      'user_id': user_id,
  }
  logger.debug(f'access_payload: {access_payload}')

  refresh_payload = {
      'token_type': 'refresh_token',
      'exp': datetime.utcnow() + timedelta(days=90),
      'user_id': user_id,
  }
  logger.debug(f'refresh_payload: {refresh_payload}')

  # TODO: algorithmもconfigに配置する
  access_token = jwt.encode(access_payload, TOKEN_SECRETE_KEY, algorithm='HS256')
  logger.debug(access_token)

  refresh_token = jwt.encode(refresh_payload, TOKEN_SECRETE_KEY, algorithm='HS256')
  logger.debug(refresh_token)

  logger.info(f'user_id: {user_id}')
  # リフレッシュトークンはログ出力しないべきと思うためコメントアウト
  # logger.info(f'refresh_token: {refresh_token}')
  db_user = get_user_by_user_id(db, user_id)
  db_user.refresh_token = refresh_token
  db.commit()
  db.refresh(db_user)

  return {'access_token': access_token, 'refresh_token': refresh_token}

def get_current_user_from_token(token: str, token_type: str, db: Session):
  """ ユーザのトークン情報を取得

  Args:
      token (str): トークン情報
      token_type (str): トークンの種類

  Raises:
      TokenException: トークンとトークンタイプが不一致の場合
      TokenException: リフレッシュトークンでDBの情報と不一致の場合

  Returns:
      User: ユーザ情報
  """

  logger.debug(f'token: {token}')
  logger.debug(f'token_type: {token_type}')

  payload = jwt.decode(token, TOKEN_SECRETE_KEY, algorithms=['HS256'])
  logger.debug(f'payload: {payload}')

  if payload['token_type'] != token_type:
    logger.error(f'token: {token}')
    logger.error(f'token_type: {token_type}')
    logger.error(f"payload_token_type: {payload['token_type']}")
    raise TokenException('トークンタイプ不一致')

  user = get_user_by_user_id(db, payload['user_id'])
  logger.debug(f'user: {user}')

  if token_type == 'refresh_token' and user.refresh_token != token:
    logger.error(f'user: {user}')
    logger.error(f'token: {token}')
    logger.error(f'token_type: {token_type}')
    raise TokenException('リフレッシュトークン不一致')

  return user

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
  """ アクセストークンをもとにユーザ取得

  Args:
      token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

  Returns:
      User: ユーザ情報
  """

  logger.debug(f'token: {token}')
  user = get_current_user_from_token(token, 'access_token', db)
  logger.debug(f'user: {user}')

  return user

async def get_current_user_with_refresh_token(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
  """ リフレッシュトークンからユーザ取得

  Args:
      token (str, optional): トークン情報. Defaults to Depends(oauth2_scheme).

  Returns:
      User: ユーザ情報
  """

  logger.debug(f'token: {token}')
  user = get_current_user_from_token(token, 'refresh_token', db)
  logger.debug(f'user: {user}')
  
  return user