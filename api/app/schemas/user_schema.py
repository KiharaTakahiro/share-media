from pydantic import BaseModel, Field, EmailStr

class UserCreate(BaseModel):
  username: str = Field(..., max_length=10, title='ユーザ名', description='ユーザ名')
  password: str = Field(..., min_length=8, max_length=20, title='パスワード', description='8文字以上で20文字以内のパスワード')
  email: EmailStr = Field(..., title='メールアドレス', description='ユーザのメールアドレス')
  age: int = Field(None,  title='年齢', description='年齢')

class UserLogin(BaseModel):
  username: str = Field(..., max_length=10, title='ユーザ名', description='ユーザ名')
  password: str = Field(..., min_length=8, max_length=20, title='パスワード', description='8文字以上で20文字以内のパスワード')
