import base64

class PresentationLayer:
    def encrypt(self, data):
        """Encrypt data using Base64 encoding."""
        return base64.b64encode(data.encode()).decode()

    def decrypt(self, data):
        """Decrypt Base64 encoded data."""
        return base64.b64decode(data.encode()).decode()
