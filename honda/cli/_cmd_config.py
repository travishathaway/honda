"""
Holds the configuration for all sub-commands
"""
import click

from honda.cli.commands.clean import clean
from honda.cli.commands.compare import compare
from honda.cli.commands.config import config
from honda.cli.commands.create import create
from honda.cli.commands.info import info
from honda.cli.commands.init import init
from honda.cli.commands.install import install
from honda.cli.commands.list import list_
from honda.cli.commands.remove import remove
from honda.cli.commands.repo import repo
from honda.cli.commands.search import search
from honda.cli.commands.update import update
from ._base import base_click_command

CMDS = (
    base_click_command(clean, "clean", help="Cleans up unused packages"),
    base_click_command(config, "config", help="Set and show configuration options"),
    base_click_command(
        compare, "compare", help="Compares two conda environments with each other"
    ),
    base_click_command(
        create,
        "create",
        help="Create a new conda environment",
        params=(click.option("no_cache", "-x", "--no-cache", is_flag=True),),
    ),
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
    base_click_command(
        repo,
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
    base_click_command(search, "search", help="Searches for packages"),
    base_click_command(update, "update", help="Update packages"),
)
