from functools import wraps

from honda.config.main import CONFIG


def app_config(func):
    """Allows us to directly inject app config to our command functions"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(CONFIG, *args, **kwargs)

    return wrapper
