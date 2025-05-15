import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("127.0.0.1", 8000)


address = ("127.0.0.1", 8001)

message = b"Message to send to the client."


sock.bind(address)

try:
    print("sending {!r}".format(message))
    sent = sock.sendto(message, server_address)

    print("waiting to receive")
    data, server = sock.recvfrom(4096)

    print("received {!r}".format(data))

finally:
    print("closing socket")
    sock.close()
