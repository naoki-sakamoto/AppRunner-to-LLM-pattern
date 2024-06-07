# Pythonのスリムバージョンのイメージをベースにする
FROM python:3.12-slim-bullseye
# コンテナ内の作業ディレクトリを設定する
WORKDIR /app
# コンテナにコピーする
COPY . .
COPY ./app ./app
# requirements.txtをコンテナにコピーする
COPY requirements.txt requirements.txt
# requirements.txtに記載されたパッケージをインストールする
RUN pip install -r requirements.txt
# コンテナのポートを外部に公開する
EXPOSE 8080
# 環境変数PORTを設定する
ENV PORT 8080
# コンテナが起動した時に実行するコマンドを設定する
ENTRYPOINT ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
