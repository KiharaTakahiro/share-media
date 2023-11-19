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

class Movie(Base):
  """ 動画の登録テーブル
  """
  __tablename__ = "movies"
  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, index=True)
  movie_name = Column(String)
  path = Column(String)
  views = Column(Integer)
  likes = Column(Integer)

  def __str__(self):
    return f'Movie [id: {self.id} user_id: {self.user_id} movie_name: {self.movie_name} path: {self.path} views: {self.views} likes: {self.likes}]'