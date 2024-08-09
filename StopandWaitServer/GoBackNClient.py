#Code sourced from https://stackoverflow.com/questions/27893804/udp-client-server-socket-in-python ,
# https://gist.github.com/tuxfight3r/1762636f788b14425c42f16d87dbc229 , and the book Computer Programing A Top Down Approach 

import socket
import time

# Setup UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = ('0.0.0.0', 12345)

# Simulate sending multiple packets
window_size = 4
base = 0
next_seq_num = 0
messages = ["Message 0", "Message 1", "Message 2", "Message 3", "Message 4"]

while base < len(messages):
# send the packets in the window
    for i in range(base, min(base + window_size, len(messages))):
        message = f"{next_seq_num},{messages[i]}"
        client_socket.sendto(message.encode(), server_address)
        print(f"Sent '{messages[i]}' with sequence number {next_seq_num} to server")
        next_seq_num += 1

    # Receive ACKs for the packets sent 
    ack_received = False
    while not ack_received:
        try:
            client_socket.settimeout(2)  # Timeout set to 2 seconds
            data, server = client_socket.recvfrom(1024)
            ack_number = int(data.decode().split()[1])
            print(f"Received ACK {ack_number} from {server}")
            base = ack_number + 1 # Move to the next ACK number
            ack_received = True # set flag to exit loop
        except socket.timeout:
            print("Timeout, resending...")
            break
client_socket.close() #close client socket
