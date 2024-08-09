# Code sourced from https://gist.github.com/Manouchehri/67b53ecdc767919dddf3ec4ea8098b20,
#  https://stackoverflow.com/questions/27893804/udp-client-server-socket-in-python, and the book Computer Programing A Top Down Approach

import socket
# Setup UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = ('0.0.0.0', 12345)

message = "Server Received" # Message to send to server
client_socket.sendto(message.encode(), server_address) 

# Receive ACK from server
acknowledged = False
while not acknowledged:
    try:
        data, server = client_socket.recvfrom(1024) # receive data from server
        print(f"Received '{data.decode()}' from {server}") #decode the data then print
        acknowledged = True # set true to exit the loop
    except socket.timeout:
        print("Timeout, resending...")  # timeout to resend message
        client_socket.sendto(message.encode(), server_address)

client_socket.close() # close client socket



