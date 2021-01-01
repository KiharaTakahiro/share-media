from .config import config
from .db import database
from .models.users.controller import router as user_route
from fastapi import FastAPI
from starlette.requests import Request
from starlette.middleware.cors import CORSMiddleware

def create_app():
  """ FastAPIのアプリケーションを生成する
  """
  # FastAPIインスタンスの生成
  conf_app = config.get_app()
  app = FastAPI(
      title=conf_app['api_name'],
      description=conf_app['api_description'],
  )

  # CORSの許可設定
  register_cors(app)
  # ルータ登録
  register_route(app)
  # イベントの登録
  register_event(app)
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

def register_event(app:FastAPI):
  @app.on_event("startup")
  async def startup():
    await database.connect()
  
  @app.on_event("shutdown")
  async def shutdown():
      await database.disconnect()

def register_middleware(app:FastAPI):
  @app.middleware("http")
  async def db_session_middleware(request: Request, call_next):
    request.state.connection = database
    response = await call_next(request)
    return response


