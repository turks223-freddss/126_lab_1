import socket

class PhysicalLayer:
    def __init__(self, role="server", host="127.0.0.1", port=5000):
        self.role = role
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_connection(self):
        """Establish a connection between sender and receiver."""
        if self.role == "server":
            self.sock.bind((self.host, self.port))
            self.sock.listen(1)
            self.conn, _ = self.sock.accept()
        else:  # Client
            self.sock.connect((self.host, self.port))

    def send_bits(self, data):
        """Convert data to binary and send it."""
        binary_data = data.encode()
        if self.role == "server":
            self.conn.sendall(binary_data)
        else:
            self.sock.sendall(binary_data)

    def receive_bits(self):
        """Receive and decode binary data."""
        if self.role == "server":
            data = self.conn.recv(1024)
        else:
            data = self.sock.recv(1024)
        return data.decode()

    def close_connection(self):
        """Close the socket."""
        self.sock.close()
