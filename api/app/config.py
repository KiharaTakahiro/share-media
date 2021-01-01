
import yaml

class Config():
  
  """ 環境の一覧
      dev:  開発環境(デフォルト)
      prod: 本番環境
      test: 自動テスト用
  """
  ENV_LIST = ['dev', 'prod', 'test']

  def get_env(self):
    """ 環境を取得し返却
        環境の設定値は以下を想定
    """
    if self.__config_data['env'] is not None:
      return self.__config_data['env']
    return ENV_LIST[0]

  def get_db_connect(self):
    """ dbの接続情報を取得し、返却する
        DBの接続情報は素直に返却する
    """
    return self.__config_data['db']

  def get_log(self):
    """ ログの情報を取得する
    """
    return self.__config_data['log']

  def get_app(self):
    """ アプリケーションの起動用の情報を取得する
    """
    return self.__config_data['app']

  def get_const(self):
    """ アプリで使用するconst系のデータを辞書形式で返却する
    """
    return self.__config['const']

  def __init__(self, config_file):
    self.__config_data = self.__load_yaml(config_file)
    self.__config_check()

  def __load_yaml(self, file_name):
    """ yamlファイルの読込処理
        ※読込エラーがある場合を考慮しないためハンドルする側で考慮すること
    """
    with open(file_name) as file:
      return yaml.safe_load(file.read())

  def __config_check(self):
    """ 取得したconfig内に想定外の値がないかをチェックする
    """
    if self.__config_data['env'] is not None:
      if not self.__config_data['env'] in self.ENV_LIST:
        raise ValueError("サポートされていない環境変数を使用しています")

def create_config():
  # TODO: だし分け方法等は後で考える
  return Config('./instance/env_dev.yml')

config = create_config()