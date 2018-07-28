# author: Izumi Sakai
# date:2018/7/26 19:08


import socket

sk = socket.socket()

address = ('127.0.0.1', 8080)
sk.connect(address)
while True:
    inp = input('>>>')
    if inp == 'q':
        break
    sk.send(bytes(inp, 'utf8'))
    data = sk.recv(1024)
    print(str(data,'utf8'))