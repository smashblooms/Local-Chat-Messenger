import socket
import os


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("127.0.0.1", 8000)

print("starting up on {}".format(server_address))

sock.bind(server_address)

while True:
    print("\nwaiting to receive message")

    data, address = sock.recvfrom(4096)

    print("received {} bytes from {}".format(len(data), address))
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print("sent {} bytes back to {}".format(sent, address))
