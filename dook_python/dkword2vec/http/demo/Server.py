#!/usr/bin/python
# encoding=utf-8
'''
基于BaseHTTPServer的http server实现，包括get，post方法，get参数接收，post参数接收。
'''
from http.server import HTTPServer, BaseHTTPRequestHandler
import io, shutil
import urllib
import os, sys
import urllib.request


class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        mpath, margs = urllib.request.splitquery(self.path)  # ?分割
        print( mpath,margs)
        self.do_action(mpath, margs)

    def do_POST(self):
        mpath, margs = urllib.request.splitquery(self.path)
        datas = self.rfile.read(int(self.headers['content-length']))
        self.do_action(mpath, datas)

    def do_action(self, path, args):
        self.outputtxt(path + args)

    def outputtxt(self, content):
        # 指定返回编码
        enc = "UTF-8"
        content = content.encode(enc)
        f = io.BytesIO()
        f.write(content)
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=%s" % enc)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        shutil.copyfileobj(f, self.wfile)

data = {'result': 'this is a test'}
host = ('localhost', 8888)


if __name__ == '__main__':
    # __init()
    server = HTTPServer(host, MyRequestHandler)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
