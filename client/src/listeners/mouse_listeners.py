from pynput import mouse
from events.mouse_event import MouseEvent
from events.events_utils import get_mouse_event_data
from events.constants import MOUSE_EVENTS


def mouse_event_listener(type):
    def handler(*args):
        event_data = get_mouse_event_data(type, args)
        mouse_event = MouseEvent(event_data)
        mouse_event.send()

    return handler


def run_listeners():
    events_listeners = {}
    for event in MOUSE_EVENTS:
        events_listeners[event] = mouse_event_listener(event)
    with mouse.Listener(**events_listeners) as listener:
        listener.join()


# # ...or, in a non-blocking fashion:
# listener = mouse.Listener(
#     on_move=on_move,
#     on_click=on_click,
#     on_scroll=on_scroll)
# listener.start()
