from datetime import datetime


def current_time(return_str: bool = True):
    if return_str:
        return f'{datetime.now():%Y-%m-%d_%H-%M-%S}'
    else:
        return datetime.now()
