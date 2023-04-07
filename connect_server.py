import asyncio

class UDPServerProtocol:
    def __init__(self):
        self.buffer = []

    def connection_made(self, transport):
        ...

    def datagram_received(self, data, addr):
        self.buffer.append((data.decode(), addr))

class UDPServer:
    async def __init__(self):
        self.loop = asyncio.get_running_loop()
        self.transport, self.protocol = await self.loop.create_datagram_endpoint(
            lambda: UDPServerProtocol(),
            local_addr=('127.0.0.1', 9999))
    async def recv(self):
        return self.protocol.buffer
    async def send(self, msg):
        self.transport.sendto(msg.encode())


class TCPServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.buffer = []

    def connection_made(self, transport):
        ...

    def data_received(self, data):
        self.buffer.append(data.decode())