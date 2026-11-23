import socket
import json


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b


functions = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}


ip = "0.0.0.0"
port = 6010

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((ip, port))
server.listen(1)

print("Server is waiting for a client...")

conn, addr = server.accept()
print("Connected to:", addr)

data = conn.recv(1024)
request = json.loads(data.decode())

func_name = request["func"]
if func_name in functions:
    result = functions[func_name](request["a"], request["b"])
else:
    result = "Unknown function"

response = json.dumps({"result": result})
conn.sendall(response.encode())

print("Result sent:", result)

conn.close()
server.close()
