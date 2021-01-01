from app.create_app import CreateApp
from app.config import Config

# よく考えるだし分けについては再度考える
config = Config('./instance/env_dev.yml')

# アプリケーションの生成
app_create = CreateApp(config)
app = app_create.create_app()