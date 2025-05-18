import socket

knock_ports = [1111, 2222, 3333]
target = "127.0.0.1"

for port in knock_ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect((target, port))
        print(f"Knocked on port {port}")
        sock.close()
    except:
        print(f"Port {port} is closed (as expected)")
