from pynput import mouse
from events.mouse_event import MouseEvent
from events.events_utils import get_mouse_event_data
from events.constants import MOUSE_EVENTS
from threading import Thread


def mouse_event_listener(event_name):
    def handler(*args):
        event_data = get_mouse_event_data(event_name, args)
        mouse_event = MouseEvent(event_data)
        mouse_event.send()

    return handler


def run_mouse_listeners():
    events_listeners = {}
    for event in MOUSE_EVENTS:
        events_listeners[event] = mouse_event_listener(event)
    with mouse.Listener(**events_listeners) as listener:
        listener.join()


def run_mouse_listener_thread():
    thread = Thread(target=run_mouse_listeners)
    thread.start()


# # ...or, in a non-blocking fashion:
# listener = mouse.Listener(
#     on_move=on_move,
#     on_click=on_click,
#     on_scroll=on_scroll)
# listener.start()
