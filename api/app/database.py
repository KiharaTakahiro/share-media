from .config import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

config_db = config.get_db_connect()

DATABASE = config_db['db_type']
USER = config_db['user']
PASSWORD = config_db['password']
HOST = config_db['host']
PORT = config_db['port']
DB_NAME = config_db['db_name']

SQLALCHEMY_DATABASE_URL = f'{DATABASE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()