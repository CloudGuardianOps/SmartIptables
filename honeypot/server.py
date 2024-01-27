import socket

def start_honeypot(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', port))
    s.listen(5)
    print(f"Honeypot running on port {port}")

    try:
        while True:
            client_socket, addr = s.accept()
            print(f"Connection from {addr} has been established.")
            client_socket.close()
    except KeyboardInterrupt:
        s.close()
