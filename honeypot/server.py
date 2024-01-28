import socket
import threading

class Honeypot:
    def __init__(self, port):
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running = False
        self.thread = None

    def start(self):
        try:
            self.socket.bind(('0.0.0.0', self.port))
            self.socket.listen(5)
            print(f"Honeypot running on port {self.port}")
            self.running = True
            self.thread = threading.Thread(target=self._listen)
            self.thread.daemon = True  # Configure le thread en mode daemon
            self.thread.start()
        except Exception as e:
            print(f"Erreur lors du démarrage du honeypot : {e}")

    def _listen(self):
        while self.running:
            try:
                client_socket, addr = self.socket.accept()
                print(f"Connection from {addr} has been established.")
                client_socket.close()
            except socket.error:
                break  # Arrête la boucle si le socket est fermé

    def stop(self):
        if self.running:
            print("Stopping Honeypot...")
            self.running = False
            self.socket.close()
            self.thread.join()
            print("Honeypot stopped.")
