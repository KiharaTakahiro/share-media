import hashlib
from app.logger import logger

def convert_hash(target:str, encode: str = "utf-8") -> str:
  """ ハッシュコード変換処理

  Args:
      target (str): ハッシュ化対象文字列
      encode (str, optional): 文字列のエンコード. Defaults to "utf-8".

  Returns:
      str: ハッシュ化後の文字列
  """
  logger.debug(f'target: {target}')
  hash_str = hashlib.sha256(target.encode(encode)).hexdigest()
  logger.debug(f'hash_str: {hash_str}')
  return hash_str