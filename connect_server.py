import socket
import threading
import json

class UDPServer():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('127.0.0.1',9999))
        self.send_count = 0
        self.buffer = []
        self.send_buffer = []
        self.recv_thread = threading.Thread(target=self._recv)
        self.recv_thread.start()
        self.send_thread = threading.Thread(target=self._send)
        self.send_thread.start()
    def _recv(self):
        while True:
            msg = self.sock.recvfrom(1024)
            self.buffer.append({'info':json.loads(msg[0].decode()), 'addr':msg[1]})
    def recv(self):
        if self.buffer:
            msg = self.buffer[:]
            self.buffer = []
            return msg
        else:
            return None
    def _send(self):
        while True:
            for msg in self.send_buffer:
                self.sock.sendto(json.dumps((msg[0], self.send_count)).encode(),msg[1])
                self.send_count += 1
                self.send_buffer.remove(msg)
    def send(self,msg,addr):
        self.send_buffer.append((msg,addr))


            

# import asyncio
# import json

# class UDPServerProtocol:
#     def __init__(self):
#         self.buffer = []

#     def connection_made(self, transport):
#         ...

#     def datagram_received(self, data, addr):
#         self.buffer.append({'info':json.loads(data.decode()), 'addr':addr})

# class UDPServer:
#     async def __init__(self):
#         self.loop = asyncio.get_running_loop()
#         self.transport, self.protocol = await self.loop.create_datagram_endpoint(
#             lambda: UDPServerProtocol(),
#             local_addr=('127.0.0.1', 9999))
#         self.send_count = 0
        
#     def recv(self):
#         msg = self.protocol.buffer[:]
#         del self.protocol.buffer[:]
#         return msg
    
#     def send(self, msg, addr):
#         self.transport.sendto(json.dumps((msg,self.send_count)).encode(), addr)
#         self.send_count += 1
