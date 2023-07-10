from events.constants import EVENTS_FOR_DEBOUNCE
from events.events_utils import debounce_event
from control.keyboard.keyboard_control import KeyboardControl
from control.mouse.mouse_control import MouseControl

# just mock for now - soon data will send through server socket
keyboard_control = KeyboardControl()
mouse_control = MouseControl()


def keyboard_control_send(event):
    keyboard_control.receive_event(event)


def mouse_control_send(event):
    mouse_control.receive_event(event)


class Event:
    def __init__(self, event_data):
        self.event_name = event_data["event_name"]
        self.type = event_data["type"]
        self.is_pressed = event_data["is_pressed"]

    def send(self):
        if self.event_name in EVENTS_FOR_DEBOUNCE:
            debounce_event(self.type, lambda: print("here timeout", self.type), 0.5)
        else:
            if self.type == "keyboard_event":
                keyboard_control_send(self)
                return

            if self.type == "mouse_event":
                mouse_control_send(self)
