import socket
import json

SERVER_IP = "127.0.0.1"
PORT = 6010

func = input("Operation (add / subtract / multiply / divide): ")
a = float(input("a: "))
b = float(input("b: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

request = {"func": func, "a": a, "b": b}
client.sendall(json.dumps(request).encode())

response = json.loads(client.recv(1024).decode())
print("Result:", response["result"])

client.close()
