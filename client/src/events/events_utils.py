from events.constants import MOUSE_EVENTS
from services.util_service import set_timeout


def get_position(data):
    return {"x": data[0], "y": data[1]}


def get_data_for_on_click(data):
    return {"is_pressed": data[len(data) - 1]}


def get_data_for_on_move(data):
    return {}


def get_data_for_on_scroll(data):
    return {"dx": data[2], "dy": data[3]}


event_data_per_type = {
    "on_click": get_data_for_on_click,
    "on_move": get_data_for_on_move,
    "on_scroll": get_data_for_on_scroll,
}


def get_mouse_event_data(type, data):
    return {
        "position": get_position(data),
        "type": type,
        **event_data_per_type[type](data),
    }


event_timers = {}


def debounce_event_sending(event_type, cb, duration=0.2):
    if event_type in event_timers:
        event_timers[event_type].cancel()

    event_timers[event_type] = set_timeout(cb, duration)
