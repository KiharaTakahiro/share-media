from pydantic import BaseModel

class Token(BaseModel):
  access_token: str
  refresh_token: str

  def __str__(self):
    return f'Token [access_token: {access_token} refresh_token: {refresh_token}]'