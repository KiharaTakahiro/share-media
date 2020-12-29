import databases
import sqlalchemy

# TODO: Configから取得して設定するように変更したいが一旦保留
DATABASE = 'postgresql'
USER = 'postgres'
PASSWORD = 'postgres'
HOST = 'localhost'
PORT = '5432'
DB_NAME = 'share_media'

DATABASE_URL = '{}://{}:{}@{}:{}/{}'.format(DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME)

# databases
database = databases.Database(DATABASE_URL, min_size=5, max_size=20)

ECHO_LOG = False

engine = sqlalchemy.create_engine(DATABASE_URL, echo=ECHO_LOG)

metadata = sqlalchemy.MetaData()

from starlette.requests import Request

# middlewareでrequestに格納したconnection(Databaseオブジェクト)を返します。
def get_connection(request: Request):
    return request.state.connection
