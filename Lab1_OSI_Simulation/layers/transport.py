import json

class TransportLayer:
    def __init__(self):
        self.sequence_number = 0

    def encapsulate(self, data):
        """Adds sequence number to the segment."""
        self.sequence_number += 1
        segment = json.dumps({"seq": self.sequence_number, "data": data})
        return segment

    def decapsulate(self, segment):
        """Extracts data and sequence number."""
        segment_data = json.loads(segment)
        return segment_data["data"]
