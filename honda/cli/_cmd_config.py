"""
Holds the configuration for all sub-commands
"""

from .clean import clean
from .compare import compare
from .config import config
from .create import create
from .info import info
from .init import init
from .install import install
from .list import list_
from .remove import remove
from .search import search
from .update import update
from ._base import base_click_command

CMDS = (
    base_click_command(clean, "clean", help="Cleans up unused packages"),
    base_click_command(config, "config", help="Set and show configuration options"),
    base_click_command(
        compare, "compare", help="Compares two conda environments with each other"
    ),
    base_click_command(create, "create", help="Create a new conda environment"),
    base_click_command(
        info, "info", help="Print information about the current environment"
    ),
    base_click_command(init, "init", help="Initializes conda for your shell"),
    base_click_command(
        install,
        "install",
        help="Installs packages to the specified environment (defaults to 'base')",
    ),
    base_click_command(
        list_, "list", help="Lists all packages in a single environment"
    ),
    base_click_command(remove, "remove", help="Removes an environment"),
    base_click_command(search, "search", help="Searches for packages"),
    base_click_command(update, "update", help="Update packages"),
)
