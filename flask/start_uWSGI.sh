#!/bin/sh
# テスト用にローカルに起動する
#export BINDDIR=/uwsgi
export ENVTEST="some words you like 1"
uwsgi \
  --http=127.0.0.1:3033 \
  --wsgi-file=./run.py \
  --callable=app \
  --pidfile=./run.pid &
sleep 1
ps xf | fgrep uwsgi | fgrep -v grep
