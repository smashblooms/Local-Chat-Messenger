import socket
import os
from faker import Faker

fake = Faker()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("127.0.0.1", 8000)

print("サーバーを起動中: {}".format(server_address))

sock.bind(server_address)

while True:
    print("--------------------------------")
    print("\nメッセージの受信を待機中...")

    data, address = sock.recvfrom(4096)

    print("{} バイトのメッセージを受信しました: {}".format(len(data), address))
    print(data)

    if data:
        data = fake.name()
        sent = sock.sendto(data.encode("utf-8"), address)
        print("sent {} バイトのメッセージを送信しました: {}".format(sent, address))
