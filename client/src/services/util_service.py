import threading


def set_timeout(cb, duration):
    timer = threading.Timer(duration, cb)
    timer.start()
    return timer
