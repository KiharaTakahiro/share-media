from starlette.requests import Request
from sqlalchemy.orm import Session
from app.logger import logger

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