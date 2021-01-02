from sqlalchemy.orm import Session

from app.models.user_model import User
from app.schemas.user_schema import UserCreate
from app.common.convert import convert_hash


# TODO: ここは本番運用では変えるか、場所を変える
HASH_SOLT = "SREMEHADIASTOL"

def create_user(db: Session, user: UserCreate):
    hashed_password = convert_hash(user.password + HASH_SOLT)
    db_user = User(email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
