#!/bin/sh
uwsgi \
  --http=127.0.0.1:3033 \
  --wsgi-file=./run.py \
  --callable=app \
  --pidfile=./run.pid &
sleep 1
ps xf | grep uwsgi
