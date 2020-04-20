#!/bin/sh
kill -INT `cat ./run.pid`
rm ./run.pid
