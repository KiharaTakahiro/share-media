from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from app.database import Base

class User(Base):
  """ ユーザのモデルを作成
  """
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True, index=True) 
  email = Column(String, index=True)
  password = Column(String)
  age = Column(Integer)
  refresh_token = Column(String)
