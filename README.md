# uWSGIサンプル

準備として
python 3.xで、FlaskとuWSGIをインストールする。

最終的には
per userでFlask+uWSGIを動かし、
UNIX Socket経由でnginx経由で公開する。

# WSGI概要

uWSGIはWSGI(ウイスキー)の実装の1つ。

[Web Server Gateway Interface - Wikipedia](https://ja.wikipedia.org/wiki/Web_Server_Gateway_Interface)


# インストール


## 準備

RHEL7系では事前に
```sh
sudo yum install python3 python3-devel python3-pip
sudo yum groupinstall "Development Tools"

# 最新のpip3を入れる
curl -kL https://bootstrap.pypa.io/get-pip.py -O
python3 get-pip.py -U --user
hash -r
rm get-pip.py
```

Debian/Ubuntu では
```sh
sudo apt install python3-pip python3-dev
```

あと、.profile等で`$HOME/.local/bin/`にパスを通しておく。

Debian/Ubuntu でもpip3は最新にしたほうがいいと思う。


# flaskとuwsgiのインストール

```sh
pip3 install --user -U flask uwsgi
```

あとは各ディレクトリの下のREADME.mdに続く。
