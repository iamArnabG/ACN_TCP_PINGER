import socket
import time

def main():
    server_ip = "172.31.0.3"
    server_port = 12000
    timeout = 1.0  # Timeout in seconds

    try:
        num_pings = int(input("Enter the number of pings to send: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    min_rtt = float("inf")
    max_rtt = 0
    total_rtt = 0
    packets_lost = 0

    for seq_num in range(1, num_pings + 1):
        message = f"PING {seq_num} {time.time()}"
        start_time = time.time()

        # Send the ping message to the server
        client_socket.sendto(message.encode(), (server_ip, server_port))

        try:
            # Set a timeout for receiving the response
            client_socket.settimeout(timeout)

            # Receive the response from the server
            response, server_address = client_socket.recvfrom(1024)
            end_time = time.time()
            rtt = end_time - start_time

            if rtt < min_rtt:
                min_rtt = rtt
            if rtt > max_rtt:
                max_rtt = rtt

            total_rtt += rtt

            print(f"response Received: {response.decode()}")
            print(f"RTT: {rtt:.6f} seconds")

        except socket.timeout:
            # Handle packet loss
            print("Request timed out")
            packets_lost += 1
+
