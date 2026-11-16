import socket

HOST = "0.0.0.0"
PORT = 5001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Waiting for a friend...")

conn, address = server.accept()
print("Connected to:", address)

message = conn.recv(1024).decode()
print("Received:", message)

reply = "aleykum selam"
conn.sendall(reply.encode())
print("Reply sent!")

conn.close()
server.close()
