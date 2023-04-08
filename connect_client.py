import asyncio, json


class EchoClientProtocol:
    def __init__(self, on_con_lost):
        self.on_con_lost = on_con_lost
        self.transport = None
        self.buffer = []

    def connection_made(self, transport):
        ...

    def datagram_received(self, data):
        self.buffer.append(json.loads(data.decode()))

    def error_received(self, exc):
        ...

    def connection_lost(self, exc):
        self.on_con_lost.set_result(True)

class UDPClient():
    async def __init__(self):
        self.loop = asyncio.get_running_loop()
        self.on_con_lost = self.loop.create_future()
        self.transport, self.protocol = await self.loop.create_datagram_endpoint(
            lambda: EchoClientProtocol(self.on_con_lost),
            remote_addr=('127.0.0.1', 9999))
    def recv(self):
        cmd_list = self.protocol.buffer[:]
        del self.protocol.buffer[:]
        return cmd_list
    def send(self, msg, addr):
        self.transport.sendto(json.dumps(msg).encode(), addr)
