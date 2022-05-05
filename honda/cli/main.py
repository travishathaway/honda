import sys

import click
from click_help_colors import HelpColorsGroup

from honda.__version__ import __version__

from honda.cli._cmd_config import CMDS


@click.group(
    invoke_without_command=True,
    cls=HelpColorsGroup,
    help_headers_color="cyan",
    help_options_color="green",
)
@click.option("--version", help="prints the version of program", is_flag=True)
@click.pass_context
def cli(ctx: click.Context, version):
    """
    `honda` is a conda compatible package manager. It is primarily meant for learning and fun.

    Please use `conda` if you actually want to get some work done!
    """
    if version is True:
        click.echo(__version__)
        sys.exit(0)

    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
    ctx.ensure_object(dict)
    ctx.obj["config"] = {}


for cmd in CMDS:
    cli.add_command(cmd)


if __name__ == "__main__":
    cli()
