import hashlib

def convert_hash(target:str):
  return hashlib.sha256(target.encode('utf-8')).hexdigest()
