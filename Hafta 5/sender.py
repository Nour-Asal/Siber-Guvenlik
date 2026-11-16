import socket

destination = "127.0.0.1"
port = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.IPPROTO_IP, 10, 0) # IP_PMTUDISC_DONT

data = b"A" * 4000
sock.sendto(data, (destination, port))
print("4000 baytlik UDP paketi gonderildi.")
