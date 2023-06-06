from listeners.mouse_listeners import run_mouse_listener_thread
from listeners.keyboard_listeners import run_keyboard_listener_thread

print("start client")
run_mouse_listener_thread()
run_keyboard_listener_thread()
