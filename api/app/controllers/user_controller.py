from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services import user_service
from .base_controller import get_db
from app.schemas.user_schema import UserCreate

router = APIRouter()

@router.post("/users/create", tags = ['user_create'])
async def users_create(user: UserCreate, db: Session = Depends(get_db)):
  user_service.create_user(db, user)
  return {'result':'success'}

# @router.post("/users/login", tags = ["user_login"])
# async def authenticate(user: UserLogin, db: Session = Depends(get_db)):
#   values = get_users_password_dict(user)
#   # query = users.select().where(and_(users.columns.username==values["username"], users.columns.password==values["password"]))
#   query = users.select().where(users.columns.username==values["username"])
#   ret = await database.fetch_one(query)
#   # print(values)
#   # print(query)
#   print(ret)
#   return {'result':'success'}

def get_users_password_dict(user):
    pwhash=convert_hash(user.password)
    values=user.dict()
    values.pop("password")
    values["password"]=pwhash
    return values
