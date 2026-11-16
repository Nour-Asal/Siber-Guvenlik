import socket

FRIEND_IP = "127.0.0.1"
PORT = 5001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((FRIEND_IP, PORT))

message = "selam"
client.sendall(message.encode())
print("Message sent:", message)

reply = client.recv(1024).decode()
print("Friend replied:", reply)

client.close()
