from pynput.mouse import Controller


class MouseControl(Controller):
    def __init__(self):
        super().__init__()

    def receive_event(self, event):
        print({"position": event.position, "is_pressed": event.is_pressed})
