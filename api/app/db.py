import databases
import sqlalchemy
from .config import config

config_db = config.get_db_connect()

DATABASE = config_db['db_type']
USER = config_db['user']
PASSWORD = config_db['password']
HOST = config_db['host']
PORT = config_db['port']
DB_NAME = config_db['db_name']

DATABASE_URL = f'{DATABASE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'

MIN_SIZE = config_db['min_size']
MAX_SIZE = config_db['max_size']

# databases
database = databases.Database(DATABASE_URL, min_size=MIN_SIZE, max_size=MAX_SIZE)

ECHO_LOG = False
engine = sqlalchemy.create_engine(DATABASE_URL, echo=ECHO_LOG)

metadata = sqlalchemy.MetaData()