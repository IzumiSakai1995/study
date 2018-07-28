# author: Izumi Sakai
# date:2018/7/29 0:21


import socket

ip_port = ('127.0.0.1',8080)

sk = socket.socket()
sk.connect(ip_port)
print('客户端启动:')
