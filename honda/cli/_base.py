from functools import wraps
from typing import Callable

import rich_click as click


def base_click_command(func, name, *args, **kwargs) -> Callable:
    """
    This gives a single sport to define our command function.
    """
    # Arguments and Options for command (configured in `_cmd_config.py`)
    params = kwargs.get("params")

    if params:
        del kwargs["params"]

    @wraps(func)
    @click.command(name, *args, **kwargs)
    def wrapper(*args_, **kwargs_):
        return func(name)(*args_, **kwargs_)

    if params:
        for param in params:
            wrapper = param(wrapper)

    return wrapper
