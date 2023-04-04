import asyncio
import sys
from minecraft.networking.connection import Connection
from minecraft.networking.packets import PingPacket, PongPacket
from minecraft.networking.types import VarInt

SERVER_ADDRESS = ('your.minecraft.server', 25565)
TIMEOUT = 3  # Timeout in seconds

async def ping_server(address):
    try:
        async with Connection(address[0], address[1], timeout=TIMEOUT) as connection:
            ping_packet = PingPacket()
            ping_packet.time = VarInt(42)
            await connection.write_packet(ping_packet)

            async def handle_pong(packet):
                await connection.disconnect()
                print(f"Received Pong from {address[0]}:{address[1]}")

            connection.register_packet_listener(handle_pong, PongPacket)

            # Wait until the connection is closed or times out
            await connection.connect_event.wait()
    except Exception as e:
        print(f"Error pinging {address[0]}:{address[1]}: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python ping_pycraft.py <server> [port]")
        sys.exit(1)

    server = sys.argv[1]
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 25565

    asyncio.run(ping_server((server, port)))

if __name__ == '__main__':
    main()
