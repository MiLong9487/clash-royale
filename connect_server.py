import asyncio
import json

class UDPServerProtocol:
    def __init__(self):
        self.buffer = []

    def connection_made(self, transport):
        ...

    def datagram_received(self, data, addr):
        self.buffer.append((json.loads(data.decode()), addr))

class UDPServer:
    async def __init__(self):
        self.loop = asyncio.get_running_loop()
        self.transport, self.protocol = await self.loop.create_datagram_endpoint(
            lambda: UDPServerProtocol(),
            local_addr=('127.0.0.1', 9999))
        
    async def recv(self):
        cmd_list = self.protocol.buffer[:]
        del self.protocol.buffer[:]
        return cmd_list
    
    async def send(self, msg):
        self.transport.sendto(json.dumps(msg).encode())
