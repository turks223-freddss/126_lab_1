class NetworkLayer:
    def __init__(self):
        self.ip_address = "192.168.1.1"

    def encapsulate(self, data):
        """Adds an IP address to the packet."""
        packet = f"{self.ip_address}|{data}"
        return packet

    def decapsulate(self, packet):
        """Extracts data from the received packet."""
        _, data = packet.split("|", 1)
        return data
