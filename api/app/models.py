from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from app.database import Base

class User(Base):
  """ ユーザのテーブル
  """
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True, index=True) 
  email = Column(String, index=True)
  password = Column(String)
  age = Column(Integer)
  refresh_token = Column(String)

  def __str__(self):
    return f'User [id: {self.id} username: {self.username} email: {self.email} password: {self.password} age: {self.age} refresh_token: {self.refresh_token}]'
