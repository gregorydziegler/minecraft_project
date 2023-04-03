pip install git+https://github.com/ammaraskar/pyCraft.git

from minecraft import authentication
from minecraft.networking.connection import Connection
from minecraft.networking.packets import serverbound

# Replace these with your Minecraft account credentials and server details
username = "your_minecraft_username"
password = "your_minecraft_password"
server_address = "your_server_address"
server_port = 25565  # Default Minecraft server port

# Authenticate with Mojang servers
auth_token = authentication.AuthenticationToken()
auth_token.authenticate(username, password)

# Function to handle chat messages received from the server
def handle_chat(chat_packet):
    print("Received:", chat_packet.json_data)

# Connect to the Minecraft server
connection = Connection(server_address, server_port, auth_token)
connection.connect()

# Register the chat message handler
connection.register_packet_listener(handle_chat, serverbound.play.ChatMessagePacket)

# Send a chat message
chat_packet = serverbound.play.ChatMessagePacket()
chat_packet.message = "/say Hello from pyCraft!"
connection.write_packet(chat_packet)

# Keep the script running until you decide to close it
try:
    while True:
        connection.run()
except KeyboardInterrupt:
    pass
finally:
    connection.disconnect()
