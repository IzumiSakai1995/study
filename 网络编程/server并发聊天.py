# author: Izumi Sakai
# date:2018/7/29 0:16


import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        print(self.client_address)
        while True:
            data = conn.recv(1024)
            print(str(data,'utf8'))
            inp = input('>>>')
            conn.sendall(bytes(inp,'utf8'))

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8080),MyServer)
    server.serve_forever()

