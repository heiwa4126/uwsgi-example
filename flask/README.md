# メモ

全部python3。事前にこのフォルダの1個上のREADME.mdを実行。

# Flask 単体

``` sh
./run.py &
./test_uwsgi.sh
```

終了は
``` sh
jobs
kill %1
```
などで。

# Flask + uWSGI で http

```sh
./start_uWSGI.sh
```
または
```sh
uwsgi uwsgi_http.ini
```
で起動。

テストは
``` sh
./test_uwsgi.sh
```

終了は
``` sh
./stop_uWSGI.sh
```

# Flask + uWSGI + nginx

uWSGIをsocket経由でnginxから呼ぶ。

まずソケット用のディレクトリを作る。
```
sudo mkdir -p /run/uwsgi
sudo chown heiwa:www-data /run/uwsgi
sudo chmod 775 /run/uwsgi
```

heiwaは作業ユーザ、www-dataはnginxの実行グループ。
`/run`は好きにアレンジしてください。

```sh
uwsgi uwsgi_socket.ini
```
で起動。`/run/uwsgi/1.sock`ができてることを確認してください。

nginxの設定例はこんな感じ。
```
  location /uwsgi {
    include uwsgi_params;
    uwsgi_pass unix:///run/uwsgi/1.sock;
  }
```

`nginx -t`で構文チェック後、
`systemctl restart nginx`などで再起動。

/uwsgi にアクセスして返事があればOK
