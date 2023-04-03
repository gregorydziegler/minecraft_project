# Import necessary libraries
from mcpi.minecraft import Minecraft
from mcpi import block

# Connect to the Minecraft server
mc = Minecraft.create()

# Set block coordinates (x, y, z)
x = 10
y = 11
z = 12

# Set the block type (e.g., STONE)
block_type = block.STONE.id

# Create a packet (set a block at the specified position)
mc.setBlock(x, y, z, block_type)

# Print a message to the console
print(f"Block set at ({x}, {y}, {z}) with block type {block_type}.")
