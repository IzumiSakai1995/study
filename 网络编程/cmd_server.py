# author: Izumi Sakai
# date:2018/7/26 22:31

import subprocess
import socket

sk = socket.socket()
address = ('127.0.0.1',8000)
sk.bind(address)
sk.listen(3)


while 1:
    conn, addr = sk.accept()
    print(addr)
    while True:
        try:
            recv_data = conn.recv(1024)    # 不许发'空'
        except Exception as e:
            break
        if not recv_data:break
        print(str(recv_data,'utf8'))
        inp = input('>>>>')
        conn.send(bytes(inp,'utf8'))
        obj = subprocess.Popen(recv_data,shell=True,stdout=subprocess.PIPE)
        obj.stdout.read()
