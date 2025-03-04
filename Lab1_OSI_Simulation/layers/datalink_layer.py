import struct

class DataLinkLayer:
    def __init__(self):
        self.mac_address = "AA:BB:CC:DD:EE:FF"

    def encapsulate(self, data):
        """Encapsulates data by adding MAC address."""
        frame = f"{self.mac_address}|{data}"
        return frame

    def decapsulate(self, frame):
        """Extracts data from a received frame."""
        _, data = frame.split("|", 1)
        return data
