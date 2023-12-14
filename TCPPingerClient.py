mport socket
import time


server_address = ("172.31.0.3" , 12000)

def ping(sequence_number):
    client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    timestamp = time.time()

    try:
        # Connect to the server
        client_socket.connect(server_address)

        client_socket.settimeout(1)

        # Send the ping message
        message = f'ping {sequence_number} {timestamp}'
        client_socket.sendall(message.encode())

        # Receive the response from the server
        response = client_socket.recv(1024).decode()



        # Calculate the round-trip time (RTT)
        rtt = time.time() - timestamp

        # Print the response and RTT
        print(f'Response from {server_address}: {response} (RTT={rtt:.3f} seconds)')

        return rtt

    except ConnectionRefusedError:
        return "Connection refused"

    except socket.timeout:
        print(f"request timed out")
        return "request timed out"

    finally:
        # Close the socket
        client_socket.close()

def main():
    # Get the number of pings from the user
    N = int(input("Enter the number of pings: "))

    # Initialize variables for RTT statistics
    min_rtt = float('inf')
    max_rtt = 0
    total_rtt = 0
    lost_packets = 0

    for sequence_number in range(1, N + 1):
        rtt = ping(sequence_number)
        if rtt == "request timed out":
            lost_packets += 1
        elif rtt == "Connection refused":
            print(f"connection refused")

        else:
            min_rtt = min(min_rtt, rtt)
            max_rtt = max(max_rtt, rtt)
            total_rtt += rtt



    # Calculate average RTT
    if N - lost_packets > 0:
        avg_rtt = total_rtt / (N - lost_packets)
    else:
        avg_rtt = 0

    # Calculate packet loss rate
    packet_loss_rate = (lost_packets / N) * 100

    # Print statistics
    print(f'\nPing statistics for {server_address[0]}:')
    print(f'  Packets: Sent = {N}, Received = {N - lost_packets}, Lost = {lost_packets} ({packet_loss_rate:.2f}% loss)')
    print(f'Approximate round-trip times in milliseconds:')
    print(f'  Minimum = {min_rtt * 1000:.3f}ms, Maximum = {max_rtt * 1000:.3f}ms, Average = {avg_rtt * 1000:.3f}ms')

if __name__ == "__main__":
    main()

