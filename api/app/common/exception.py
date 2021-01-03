from fastapi import HTTPException

class APIBaseException(HTTPException):
  """ アプリケーションの全体で使用するエクセプションの基底クラス
  """
  def __init__(self, status_code, detail):
    super(APIBaseException, self).__init__(status_code=status_code, detail=detail)

class TokenException(APIBaseException):
  """ トークンでのエラーが発生した場合のエクセプション
  """
  def __init__(self, msg):
    super(TokenException, self).__init__(status_code=401, detail=msg)

class ValidationException(APIBaseException):
  """ バリデーションエラーが発生した場合のエクセプション
  """
  def __init__(self, msg):
    super(ValidationException, self).__init__(status_code=422, detail=msg)

class APIException(APIBaseException):
  """ API内でのモデルの不一致等で起こる想定外エラーの場合のエクセプション
  """
  def __init__(self, msg):
    super(APIException, self).__init__(status_code=500, detail=msg)
