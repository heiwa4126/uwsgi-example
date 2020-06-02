#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable-msg=C0103, C0111

from flask import Flask, jsonify
import os

BINDDIR = os.environ.get('BINDDIR','')    # nginx等でlocationに書くパス
MSG1 = os.environ.get('ENVTEST','test')   # test message

app = Flask(__name__)


@app.route(BINDDIR+'/')
def api_sample():
    """
    APIサンプル
    :return:
    """
    result = {"code": "001", "name": "apple", "msg1": MSG1}
    return jsonify(ResultSet=result)

@app.route(BINDDIR+'/uwsgi/')
def api_uwsgi():
    """
    APIサンプル
    :return:
    """
    result = {"code": "002", "name": "orange", "msg1": MSG1}
    return jsonify(ResultSet=result)


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=3033)
    # Flaskのデバッグオプションについては以下を参照
    # https://www.subarunari.com/entry/2017/09/26/002940
