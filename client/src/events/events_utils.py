from events.constants import MOUSE_EVENTS

event_data_per_type = {}
for event in MOUSE_EVENTS:
    event_data_per_type[event] = event


def get_mouse_event_data(type, data):
    print(event_data_per_type[type])
