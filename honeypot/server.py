import socket
import threading
import signal

class Honeypot:
    def __init__(self, port):
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running = False
        self.thread = None

    def start(self):
        self.socket.bind(('0.0.0.0', self.port))
        self.socket.listen(5)
        print(f"Honeypot running on port {self.port}")
        self.running = True
        self.thread = threading.Thread(target=self._listen)
        self.thread.start()

    def _listen(self):
        try:
            while self.running:
                client_socket, addr = self.socket.accept()
                print(f"Connection from {addr} has been established.")
                client_socket.close()
        finally:
            self.socket.close()

    def stop(self):
        print("Stopping Honeypot...")
        self.running = False
        self.socket.close()
        self.thread.join()



