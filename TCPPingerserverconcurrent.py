mport socket
import random
import threading
def handle_client(client_socket):
    try:

        # Receive the ping request from the client
        data = client_socket.recv(1024).decode()

        if data.startswith("ping"):
            # Extract sequence number and timestamp from the ping request
            parts = data.split()
            sequence_number = parts[1]
            timestamp = parts[2]

            # Send a response back to the client
            response_message = data.upper()
            rand = random.randint(0,10)
            if rand > 3 :

                client_socket.sendall(response_message.encode())
                print(f"Sent response: {response_message} \n ")

    except Exception as e:
        print(f"Exception: {e}")
    finally:
        # Close the client socket
        client_socket.close()



# Define the server address (use the same address as in the client)
server_address = ('172.31.0.3', 12000)

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address
server_socket.bind(server_address)

# Listen for incoming connections (maximum 1 connection in the queue)
server_socket.listen(1)

print(f"TCP server is listening on {server_address[0]}:{server_address[1]}")

while True:
    # Wait for a connection from the client
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]} \n")

    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

