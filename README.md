# share-media
メディアの共有用サイト

# 開発環境構築
・前提  
share_media用のデータベースを```CREATE DATABASE```で作成しておく(テーブルはapi起動時にマイグレートされるため不要)  
・手順  
１．apiディレクトリにinstanceディレクトリを生成  
２．instanceディレクトリにenv_dev.ymlを生成して配置する  
env_dev.ymlは下記を参考に作成する(DB部分は#以降の内容にならって前提で作成したdatabaseへの接続情報で記載してください)  
```yaml
env: dev
app:
  api_name: share-media
  api_description: media share api
db:
  db_type: 'postgresql'  # DBの種類
  user: 'user_name'      # DBのユーザ名
  password: password'    # パスワード
  host: 'localhost'      # DBのホスト
  port: '5432'           # DBのポート
  db_name: 'share_media' # DB名
log:
  version: 1
  formatters:
    default:
      format: '%(asctime)s %(levelname)s %(name)s %(message)s'
      datefmt: '%Y/%m/%d %I:%M:%S'
  handlers:
    console:
      class: logging.StreamHandler
      level: DEBUG
      formatter: default
      stream: ext://sys.stdout
  loggers:
    app_logger:
      level: DEBUG
      handlers: [console]
      propagate: no
  root:
    level: DEBUG
    handlers: [console]
```
  
３．apiディレクトリにて
```
$ pipenv install
$ pipenv run start
```
を実行してapiを起動する  

４．webディレクトリにて
```
$ npm install
$ npm run dev
```
コマンドを実行してフロントを起動する  
