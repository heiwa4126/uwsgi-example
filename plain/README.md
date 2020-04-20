# uWSGIサンプル

Flaskを使わないWSGIのサンプル。

まず、1個上のREADME.mdを読んでuwsgiをインストールした後に:

* `start_uwsgi.sh`で開始 - http://127.0.0.1:3031 で待受開始
* `test_uwsgi.sh`でテスト
* `stop_uwsgi.sh`で停止 - PID fileで止める方式。INTで止まる。デフォルトのTERMだとリロード
