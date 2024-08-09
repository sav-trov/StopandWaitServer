#Code sourced from https://stackoverflow.com/questions/27893804/udp-client-server-socket-in-python ,
# https://gist.github.com/tuxfight3r/1762636f788b14425c42f16d87dbc229 , and the book Computer Programing A Top Down Approach 
import socket

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 12345)) # assign the IP address and port number 

print("Server is ready")

expected_sequence_number = 0

while True:
    # Receive the data and sequence number from client
    data, client_address = server_socket.recvfrom(1024)
# Extract the sequence number and message received
    received_sequence_number = int(data.decode().split(',')[0])
    message = data.decode().split(',')[1]

    print(f"Received '{message}' with sequence number {received_sequence_number} from {client_address}")

#check if the received sequence number matches the expected sequence number
    if received_sequence_number == expected_sequence_number:
        # Send ACK to client
        ack_message = f"ACK {expected_sequence_number}"
        server_socket.sendto(ack_message.encode(), client_address)
        print(f"Sent ACK {expected_sequence_number} to {client_address}")
        expected_sequence_number += 1   # move to the next sequence number
    else:
	# if a out of order packet is received its discarded
        print(f"Discarded packet {received_sequence_number} (out of order)")
# close the server scoket
server_socket.close()
