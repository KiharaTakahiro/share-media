from .config import Config
from .db import database
from .models.users.controller import router as user_route
from fastapi import FastAPI
from starlette.requests import Request
from starlette.middleware.cors import CORSMiddleware

class CreateApp():
  """ アプリケーションの作成に関わるクラス
  """

  def __init__(self, config:Config):
    self.__config = config

  def create_app(self):
    """ FastAPIのアプリケーションを生成する
    """
    # FastAPIインスタンスの生成
    conf_app = self.__config.get_app()
    app = FastAPI(
        title=conf_app['api_name'],
        description=conf_app['api_description'],
    )

    # CORSの許可設定
    self.register_cors(app)
    # ルータ登録
    self.register_route(app)
    # イベントの登録
    self.register_event(app)
    # ミドルウェアの登録
    self.register_middleware(app)
    return app

  def register_cors(self, app:FastAPI):
    """ WEBのNext.jsと疎通するためにCORSの許可設定を登録する
    """
    app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"])
  
  def register_route(self, app:FastAPI):
    """ APIルータを登録する
    """
    app.include_router(user_route)

  def register_event(self, app:FastAPI):
    @app.on_event("startup")
    async def startup():
      await database.connect()
    
    @app.on_event("shutdown")
    async def shutdown():
        await database.disconnect()
  
  def register_middleware(self, app:FastAPI):
    @app.middleware("http")
    async def db_session_middleware(request: Request, call_next):
      request.state.connection = database
      response = await call_next(request)
      return response


