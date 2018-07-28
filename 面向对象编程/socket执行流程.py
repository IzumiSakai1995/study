# author: Izumi Sakai
# date:2018/7/2423:00


import socketserver

obj = socketserver.ThreadingTCPServer(1,2)
obj.serve_forever()