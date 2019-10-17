# -*- coding: utf-8 -*-
# 2017/11/25 20:15
import socketserver

class MyServer(socketserver .BaseRequestHandler):
    def handle(self):
        # print self.request,self.client_address,self.server
        conn = self.request
        conn.sendall(bytes('欢迎致电 10086，0转人工服务.',encoding='utf8'))
        Flag = True
        while Flag:
            data = conn.recv(1024)
            data = str(data, encoding='utf8')
            if data == 'exit':
                Flag = False
            elif data == '0':
                conn.sendall(bytes('通过可能会被录音',encoding='utf8'))
            else:
                conn.sendall(bytes('请重新输入.',encoding='utf8'))

if __name__ == '__main__':
    server = socketserver .ThreadingTCPServer(('127.0.0.1',8009),MyServer)
    server.serve_forever()