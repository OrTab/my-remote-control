from events.constants import MOUSE_EVENTS
from services.util_service import set_timeout
import threading


# ------mouse--------
is_mouse_pressed = False


def get_position(data):
    return {"x": data[0], "y": data[1]}


def handle_on_click(data):
    global is_mouse_pressed
    is_mouse_pressed = data[len(data) - 1]
    return {}


def get_data_for_on_move(data):
    return {}


def get_data_for_on_scroll(data):
    return {"dx": data[2], "dy": data[3]}


event_data_per_type = {
    "on_click": handle_on_click,
    "on_move": get_data_for_on_move,
    "on_scroll": get_data_for_on_scroll,
}


def get_mouse_event_data(event_name, data):
    return {
        **event_data_per_type[event_name](data),
        "position": get_position(data),
        "type": "mouse_event",
        "event_name": event_name,
        "is_pressed": is_mouse_pressed,
    }


# ------keyboard--------


def get_keyboard_event_data(event_name, key):
    return {
        "key": key,
        "is_pressed": event_name == "on_press",
        "type": "keyboard_event",
        "event_name": event_name,
    }


# -------shared---------
event_timers = {}
event_timers_lock = threading.Lock()


def debounce_event_sending(event_type, cb, duration=0.2):
    with event_timers_lock:
        if event_type in event_timers:
            event_timers[event_type].cancel()

        event_timers[event_type] = set_timeout(cb, duration)
