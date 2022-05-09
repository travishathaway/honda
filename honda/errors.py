from typing import Union

from click import ClickException
from rich.console import Text


class RichClickException(ClickException):
    def __init__(self, message: Union[str, Text]):
        super().__init__(message)
