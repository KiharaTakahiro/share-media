import logging
import inspect
from .config import Config, config

class Logger():
  def __init__(self, config: Config):
    self._config = config.get_log()
    self.__create_logger()

  def __create_logger(self):
    # TODO: configをもっと吸収する予定
    logging.config.dictConfig(self._config)
    self._logger = logging.getLogger("app_logger")

  def debug(self, message):
    file_name = inspect.stack()[1].filename
    function_name = inspect.stack()[1].function
    self._logger.debug(f'{file_name}#{function_name}: {message}')

  def info(self, message):
    file_name = inspect.stack()[1].filename
    function_name = inspect.stack()[1].function
    self._logger.info(f'{file_name}#{function_name}: {message}')
  
  def warn(self, message):
    file_name = inspect.stack()[1].filename
    function_name = inspect.stack()[1].function
    self._logger.warn(f'{file_name}#{function_name}: {message}')

  def error(self, message):
    file_name = inspect.stack()[1].filename
    function_name = inspect.stack()[1].function
    self._logger.error(f'{file_name}#{function_name}: {message}')

logger = Logger(config)