import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("127.0.0.1", 8000)

address = ("127.0.0.1", 8001)


sock.bind(address)

try:
    message = input("送信するメッセージを入力してください: ")
    message = message.encode("utf-8")

    print("{!r}".format(message) + "を送信中...")
    sent = sock.sendto(message, server_address)

    print("サーバーからの返答を待機中...")
    data, server = sock.recvfrom(4096)

    print("サーバーから次のメッセージを受信しました: {!r}".format(data))

finally:
    print("ソケットを閉じています...")
    sock.close()
