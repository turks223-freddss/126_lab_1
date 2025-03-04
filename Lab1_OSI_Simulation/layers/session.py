class SessionLayer:
    def __init__(self):
        self.session_active = False

    def start_session(self):
        """Start a session."""
        self.session_active = True
        return "Session Started"

    def end_session(self):
        """End a session."""
        self.session_active = False
        return "Session Ended"

    def encapsulate(self, data):
        """Attach session information."""
        return f"SESSION_ACTIVE|{data}" if self.session_active else "NO_SESSION"

    def decapsulate(self, message):
        """Extracts data if session is active."""
        if message.startswith("SESSION_ACTIVE"):
            return message.split("|", 1)[1]
        return "Session Not Active"
