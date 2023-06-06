from events.event import Event


class MouseEvent(Event):
    def __init__(self, event_data):
        super().__init__(event_data)
        self.position = event_data["position"]
