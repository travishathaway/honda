"""
Holds the configuration for all sub-commands
"""
import click

import importlib
from typing import Callable

from honda.cli._base import base_click_command


def get_cmd(cmd: str) -> Callable:
    """
    We have this command here to speed up the CLI program.
    It essentially lazy loads the modules for the various sub-commands.

    All command modules follow these rules:
     - Inside the module, there is a main function that is identical to the module name

    """
    mod = importlib.import_module(f"honda.cli.commands.{cmd}")
    cmd_func = getattr(mod, cmd)
    return cmd_func


CMDS = (
    base_click_command(get_cmd, "clean", help="Cleans up unused packages"),
    base_click_command(get_cmd, "config", help="Set and show configuration options"),
    base_click_command(
        get_cmd, "compare", help="Compares two conda environments with each other"
    ),
    base_click_command(
        get_cmd,
        "create",
        help="Create a new conda environment",
        params=(
            click.option("no_cache", "-x", "--no-cache", is_flag=True),
            click.option("channels", "-c", "--channel", multiple=True),
        ),
    ),
    base_click_command(
        get_cmd, "info", help="Print information about the current environment"
    ),
    base_click_command(get_cmd, "init", help="Initializes conda for your shell"),
    base_click_command(
        get_cmd,
        "install",
        help="Installs packages to the specified environment (defaults to 'base')",
    ),
    base_click_command(
        get_cmd, "list", help="Lists all packages in a single environment"
    ),
    base_click_command(get_cmd, "remove", help="Removes an environment"),
    base_click_command(
        get_cmd,
        "repo",
        help="Download the most recent version of repo data",
        params=(
            click.option(
                "channel",
                "-c",
                "--channel",
                help="Override default channels with ones specified here",
            ),
        ),
    ),
    base_click_command(get_cmd, "search", help="Searches for packages"),
    base_click_command(get_cmd, "update", help="Update packages"),
)
