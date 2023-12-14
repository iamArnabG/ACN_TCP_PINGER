import random
from socket import *
# Create a UDP socket  
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('172.31.0.3', 12000))

while True:
    # Generate a random number between 0 to 11 (both included)  
    rand = random.randint(0, 11)
    message, address = serverSocket.recvfrom(1024)
    # Capitalize the message from the client  
    message = message.upper()
    if rand < 4:
        continue
    serverSocket.sendto(message, address)

