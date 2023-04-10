import socket
import threading
import json

class UDPClient():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_addr = ('127.0.0.1',9999)
        self.buffer = None
        self.recv_count = -1
        self.msg = None
        self.sock.sendto(json.dumps('connect to server').encode(),self.server_addr)
        self.send_thread = threading.Thread(target=self._send)
        self.send_thread.start()
        self.recv_thread = threading.Thread(target=self._recv)
        self.recv_thread.start()
    def _recv(self):
        while True:
            msg, addr = self.sock.recvfrom(1024)
            msg = json.loads(msg.decode())
            if msg[1] > self.recv_count:
                self.buffer = msg[0]
                self.recv_count = msg[1]
    def recv(self):
        if self.buffer:
            msg = self.buffer
            self.buffer = None
            return msg
        else:
            return None
    def _send(self):
        while True:
            if self.msg:
                self.sock.sendto(json.dumps(self.msg).encode(),self.server_addr)
                self.msg = None
    def send(self,msg):
        self.msg = msg


# import asyncio, json


# class EchoClientProtocol:
#     def __init__(self, on_con_lost):
#         self.on_con_lost = on_con_lost
#         self.transport = None
#         self.buffer = None
#         self.recv_count = -1

#     def connection_made(self, transport):
#         ...

#     def datagram_received(self, data):
#         msg = json.loads(data.decode())
#         if msg[1] > self.recv_count:
#             self.buffer = msg[0]
#             self.recv_count = msg[1]

#     def error_received(self, exc):
#         ...

#     def connection_lost(self, exc):
#         self.on_con_lost.set_result(True)

# class UDPClient():
#     async def __init__(self):
#         self.loop = asyncio.get_running_loop()
#         self.on_con_lost = self.loop.create_future()
#         self.transport, self.protocol = await self.loop.create_datagram_endpoint(
#             lambda: EchoClientProtocol(self.on_con_lost),
#             remote_addr=('127.0.0.1', 9999))
        
#     def recv(self):
#         msg = self.protocol.buffer[:]
#         del self.protocol.buffer[:]
#         return msg
    
#     def send(self, msg):
#         self.transport.sendto(json.dumps(msg).encode())
