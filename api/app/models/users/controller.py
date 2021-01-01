from fastapi import APIRouter, Depends
from .model import users
from .schema import UserCreate
from databases import Database
from app.models.base_controller import get_connection
from app.common.convert import convert_hash

router = APIRouter()

# TODO: ここに書きたくない
def get_users_insert_dict(user):
    pwhash=convert_hash(user.password)
    values=user.dict()
    values.pop("password")
    values["password"]=pwhash
    return values

@router.post("/users/create", tags = ['user_create'])
async def users_create(user: UserCreate, database: Database = Depends(get_connection)):
  query = users.insert()
  values = get_users_insert_dict(user)
  ret = await database.execute(query, values)
  return {'test':'test'}