from sqlalchemy.orm import Session

from app.models import User
from app.schemas.user_schema import UserCreate, UserLogin
from app.common.convert import convert_hash


# TODO: ここは本番運用では変えるか、場所を変える
HASH_SOLT = "SREMEHADIASTOL"

def create_user(db: Session, user: UserCreate):
    hashed_password = convert_hash(user.password + HASH_SOLT)
    db_user = User(username=user.username, email=user.email, password=hashed_password, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_user_name(db: Session, username: str):
    return db.query(User).filter(User.username==username).first()

def get_user_by_user_login(db: Session, user: UserLogin):
    hashed_password = convert_hash(user.password + HASH_SOLT)
    return db.query(User).filter(User.username==user.username, User.password==hashed_password).first()