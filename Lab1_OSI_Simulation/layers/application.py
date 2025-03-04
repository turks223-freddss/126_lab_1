class ApplicationLayer:
    def generate_request(self, message):
        """Create an HTTP-like request."""
        return f"GET / {message}"

    def process_response(self, response):
        """Process HTTP-like response."""
        return f"Response received: {response}"
