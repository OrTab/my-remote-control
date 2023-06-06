from pynput import keyboard
from events.keyboard_event import KeyboardEvent
from events.events_utils import get_mouse_event_data, get_keyboard_event_data
from events.constants import KEYBOARD_EVENTS
from threading import Thread


def keyboard_event_listener(event_name):
    def handler(key):
        try:
            key = key.char
        except AttributeError:
            key = key
        event_data = get_keyboard_event_data(event_name, key)
        keyboard_event = KeyboardEvent(event_data)
        keyboard_event.send()

    return handler


def run_keyboard_listeners():
    events_listeners = {}
    for event in KEYBOARD_EVENTS:
        events_listeners[event] = keyboard_event_listener(event)
    with keyboard.Listener(**events_listeners) as listener:
        listener.join()


def run_keyboard_listener_thread():
    thread = Thread(target=run_keyboard_listeners)
    thread.start()


# # ...or, in a non-blocking fashion:
# listener = mouse.Listener(
#     on_move=on_move,
#     on_click=on_click,
#     on_scroll=on_scroll)
# listener.start()
