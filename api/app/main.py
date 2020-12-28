import uvicorn
from fastapi import FastAPI
from config import Config
from controllers import users_controller

# configファイルを読み込み
config = Config('./instance/env_dev.yml')
conf_app = config.get_app()

# FastAPIインスタンスの生成
app = FastAPI(
    title=conf_app['api_name'],
    description=conf_app['api_description'],
)

# ルータの登録
app.include_router(users_controller.router)

# アプリケーションの起動
if __name__ == '__main__':
  uvicorn.run(app, port=conf_app['port'])