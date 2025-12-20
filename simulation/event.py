class Event:
    def __init__(self, time, event_type, payload):
        self.time = time
        self.type = event_type
        self.payload = payload

    def __lt__(self, other):
        return self.time < other.time
