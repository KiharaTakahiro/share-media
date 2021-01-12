from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
from app.common.exception import ValidationException
from .base_controller import get_db
from app.schemas.token_schema import Token
from app.logger import logger
from app.services import user_service
from pathlib import Path
from tempfile import NamedTemporaryFile
import shutil
import os
import datetime

router = APIRouter()

# TODO: 処理は今後サービスに移す
def save_upload_file_tmp(upload_file: UploadFile) -> Path:
  try:
    logger.debug(f'upload_file: {upload_file}')
    directory_name = './upload_files/{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now())
    logger.debug(f'directory_name: {directory_name}')
    os.mkdir(directory_name)
    suffix = Path(upload_file.filename).suffix
    logger.debug(f'suffix: {suffix}')
    with open(f"./{directory_name}/origin" + suffix , "wb") as buffer:
      shutil.copyfileobj(upload_file.file, buffer)
      buffer_name = Path(buffer.name)
      logger.debug(f'buffer_name: {buffer_name}')
  except Exception as e:
    logger.error(f'{e}')
  finally:
    upload_file.file.close()

  return buffer_name

@router.post("/movies/upload_file")
async def movies_create(file: UploadFile = File(...)):
  save_upload_file_tmp(file)
  return {'result':'success'}