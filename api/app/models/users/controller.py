from fastapi import APIRouter, Depends
from .model import users
from .schema import UserCreate
from db import get_connection
from databases import Database
import hashlib

router = APIRouter()

# TODO: ここに書きたくない
def get_users_insert_dict(user):
    pwhash=hashlib.sha256(user.password.encode('utf-8')).hexdigest()
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