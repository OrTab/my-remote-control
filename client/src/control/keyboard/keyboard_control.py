from pynput.keyboard import Key, Controller


class KeyboardControl(Controller):
    def __init__(self):
        super().__init__()

    def receive_event(self, event):
        print({"key": event.key, "is_pressed": event.is_pressed})
