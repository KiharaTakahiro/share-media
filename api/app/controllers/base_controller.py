from starlette.requests import Request
from sqlalchemy.orm import Session
from app.logger import logger
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from app.services.user_service import get_current_user_from_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db(request: Request)-> Session:
    """ DBの取得処理

    Args:
        request (Request): request

    Returns:
        Session: DBのセッション情報を返却する
    """
    logger.debug(f'request: {request}')
    db = request.state.db
    logger.debug(f'db: {db}')
    return db

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