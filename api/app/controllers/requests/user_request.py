from pydantic import BaseModel, Field, EmailStr

class RegisterUserRequest(BaseModel):
  name: str = Field(..., max_length=50, title='ユーザ名', description='ユーザ名')
  password: str = Field(..., min_length=8, max_length=20, title='パスワード',description='8文字以上で20文字以内のパスワード')
  email: EmailStr
  age: int = Field(None,  title='年齢', description='年齢')
