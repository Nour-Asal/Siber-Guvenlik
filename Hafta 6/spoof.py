from scapy.all import IP, ICMP, send

# Forging source IP (172.16.31.20) while sending to loopback (127.0.0.1)
paket = IP(src="172.16.31.20", dst="127.0.0.1")/ICMP()
send(paket, count=1)
