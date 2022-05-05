from functools import wraps
from typing import Callable

import click
from click_help_colors import HelpColorsCommand


def base_click_command(func, name, *args, **kwargs) -> Callable:
    """
    This gives a single sport to define our command function.
    """
    # Arguments and Options for command (configured in `_cmd_config.py`)
    params = kwargs.get("params")

    if params:
        del kwargs["params"]

    @wraps(func)
    @click.command(
        name,
        cls=HelpColorsCommand,
        help_headers_color="cyan",
        help_options_color="green",
        help_options_custom_colors={"--count": "red", "--subtract": "green"},
        **kwargs
    )
    def wrapper(*args_, **kwargs_):
        return func(name)(*args_, **kwargs_)

    if params:
        for param in params:
            wrapper = param(wrapper)

    return wrapper
