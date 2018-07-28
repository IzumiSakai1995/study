# author: Izumi Sakai
# date:2018/7/26 18:02


import socket

sk = socket.socket()
address = ('127.0.0.1',8000)
sk.connect(address)

# client 下的方法   connect send() recv() sendall()

data = sk.recv(1024)   # 阻塞 等待服务端
print(str(data,'utf8'))


sk.close()