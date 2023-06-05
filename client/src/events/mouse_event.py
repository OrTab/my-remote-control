from events.event import Event


class MouseEvent(Event):
    def __init__(self, event_data):
        super().__init__({"type": event_data["type"]})
        self.position = event_data["position"]
        # self.is_pressed = event_data["is_pressed"]
