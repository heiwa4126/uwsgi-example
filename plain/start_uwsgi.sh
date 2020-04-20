#!/bin/sh
uwsgi \
  --plugin http,python \
  --http 127.0.0.1:3031 \
  --wsgi-file ./run.py \
  --pidfile ./run.pid &
sleep 1
ps xf | grep uwsgi
