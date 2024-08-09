# Code sourced from https://gist.github.com/Manouchehri/67b53ecdc767919dddf3ec4ea8098b20,
#  https://stackoverflow.com/questions/27893804/udp-client-server-socket-in-python, and the book Computer Programing A Top Down Approach

import socket

# Setup UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 12345)) #assign server address and port

print("Server is ready")

while True:
    # Receive data from client
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received '{data.decode()}' from {client_address}") #decode data and print

    # Simulate ACK  and send back the same message
    server_socket.sendto(data, client_address)
