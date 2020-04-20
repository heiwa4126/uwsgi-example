#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable-msg=C0103, C0111

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    rvalue = b"Hello World\n"
    rvalue += b"Test\n"
    rvalue += b"Apr/14/2020\n"
    return [rvalue]
