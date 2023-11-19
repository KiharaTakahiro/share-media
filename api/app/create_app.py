from .config import config
from .controllers.user_controller import router as user_route
from .controllers.movie_controller import router as movie_route
from fastapi import FastAPI, Response
from starlette.requests import Request
from starlette.middleware.cors import CORSMiddleware
from app.database import SessionLocal, engine
from app.models import Base
from .logger import logger
from app.common.exception import APIException, ValidationException

def create_app():
  """ FastAPIのアプリケーションを生成する
  """
  logger.debug("アプリケーション生成ロジック開始")

  Base.metadata.create_all(bind=engine)
  logger.debug("マイグレーション完了")

  # FastAPIインスタンスの生成
  conf_app = config.get_app()
  logger.debug(f'conf_app: {conf_app}')

  app = FastAPI(
      title=conf_app['api_name'],
      description=conf_app['api_description'],
  )

  # CORSの許可設定
  register_cors(app)
  
  # ルータ登録
  register_route(app)
  
  # ミドルウェアの登録
  register_middleware(app)
  return app

def register_cors(app:FastAPI):
  """ WEBのNext.jsと疎通するためにCORSの許可設定を登録する
  """
  app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])
  
def register_route(app:FastAPI):
  """ APIルータを登録する
  """
  app.include_router(user_route)
  app.include_router(movie_route)

def register_middleware(app:FastAPI):
  @app.middleware("http")
  async def db_session_middleware(request: Request, call_next):
    logger.debug(f'request: {request}')
    response = Response("Internal server error", status_code=500)
    try:
      request.state.db = SessionLocal()
      response = await call_next(request)
    except ValidationException as e:
      raise e
    except TokenException as e:
      raise e
    except Exception as e:
      raise APIException(f'{e}')
    finally:
      logger.debug(f'response: {response}')
      request.state.db.close()
    return response