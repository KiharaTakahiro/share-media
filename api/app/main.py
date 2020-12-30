import uvicorn
from fastapi import FastAPI
from config import Config
from models.users.controller import router as user_route
from db import database
from starlette.middleware.cors import CORSMiddleware

# configファイルを読み込み
config = Config('./instance/env_dev.yml')
conf_app = config.get_app()

# FastAPIインスタンスの生成
app = FastAPI(
    title=conf_app['api_name'],
    description=conf_app['api_description'],
)

# cors対策
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# 起動時にDatabaseに接続する。
@app.on_event("startup")
async def startup():
    await database.connect()

# 終了時にDatabaseを切断する。
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# ルータの登録
app.include_router(user_route)

# # アプリケーションの起動
# if __name__ == '__main__':
#   uvicorn.run(app, port=conf_app['port'])

from starlette.requests import Request

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.connection = database
    response = await call_next(request)
    return response