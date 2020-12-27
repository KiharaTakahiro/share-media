import uvicorn
from fastapi import FastAPI
from config import Config
from controllers import users_controller

config = Config('./instance/env_dev.yml')
app = FastAPI(
    title="メディア共有API",
    description="メディア共有用のAPI機能を提供するAPIです。",
)

app.include_router(users_controller.router)

if __name__ == '__main__':
  conf_app = config.get_app()
  uvicorn.run(app, port=conf_app['port'])