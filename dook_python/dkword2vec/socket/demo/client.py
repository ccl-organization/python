# -*- coding: utf-8 -*-
# 2017/11/25 20:16
import socket
ip_port = ('127.0.0.1',8009)
sk = socket.socket()
sk.connect(ip_port)
sk.settimeout(60000)

while True:
    data = sk.recv(1024)
    data = str(data, encoding='utf8')
    print('receive:',data)
    inp = input('please input:')
    sk.sendall(bytes(inp,encoding="utf8"))
    if inp == 'exit':
        break

sk.close()