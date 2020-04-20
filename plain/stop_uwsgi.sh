#!/bin/sh
PIDFILE=./run.pid
kill -INT `cat "$PIDFILE"`
rm "$PIDFILE"
