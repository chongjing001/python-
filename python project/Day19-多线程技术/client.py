import socket

client = socket.socket()

client.connect(("10.7.187.149", 9001))

while True:
    message = input("***")
    client.send(message.encode("utf-8"))
