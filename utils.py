from datetime import datetime


def current_time():
    return f'{datetime.now():%Y-%m-%d_%H-%M-%S}'
