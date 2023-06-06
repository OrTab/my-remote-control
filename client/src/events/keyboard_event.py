from events.event import Event


class KeyboardEvent(Event):
    def __init__(self, event_data):
        super().__init__({"type": event_data["type"]})
