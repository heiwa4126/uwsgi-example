#!/bin/sh
#本番用. nginxのwsgiで使うとき
export BINDDIR=/uwsgi
export ENVTEST="some words you like 2"
uwsgi ./uwsgi_sock.ini --enable-threads &
sleep 1
ps xf | fgrep uwsgi | fgrep -v grep
