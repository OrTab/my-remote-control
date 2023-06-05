from events.constants import EVENTS_FOR_DEBOUNCE
from events.events_utils import debounce_event_sending


class Event:
    def __init__(self, event_data):
        self.type = event_data["type"]

    def send(self):
        if self.type in EVENTS_FOR_DEBOUNCE:
            debounce_event_sending(
                self.type, lambda: print("here timeout", self.type), 0.5
            )
        else:
            print("send", self.type)
