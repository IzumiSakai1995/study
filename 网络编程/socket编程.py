# author: Izumi Sakai
# date:2018/7/2616:50


import socket


'''
family(AF_INET ipv4  ipv6 : AF_INET6) , type(SOCK_STREAM = 1:TCP,SOCK_DGRAM(数据socket for UDP )= 2  SOCK_RAW = 3 SOCK_RDM = 4)

AF_INET 服务器之间
AF_UNIX UNIX进程间
'''
sk = socket.socket()

address = ('127.0.0.1',8000)

sk.bind(address)   # 绑定IP地址和端口

sk.listen(3)  # 最大排队数
print('waiting............')
conn,addr = sk.accept()  # 阻塞  等待客户端连接

print(conn)
# (<socket.socket fd=752, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8000)
# , raddr=('127.0.0.1', 57542)>, ('127.0.0.1', 57542))
# 两个sk 没有关系
# server 下的方法 bind listhen accpet send() recv() sendall()
inp = input('>>>')
conn.send(bytes(inp,'utf8'))   # 传送的内容一定得是bytes类型

conn.close()

'''
方法
sk.setbolcking(bool) 是否阻塞（默认True）
sk.connect_ex 同connect 有返回值
sk.sendto
sk.settimeout  连接维持时间 单位为秒s
sk.fileno  套接字的文件描述符
'''