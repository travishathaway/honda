import sys

# import click
import rich_click as click

from honda.__version__ import __version__
from honda.config.constants import APP_NAME
from honda.cli._cmd_config import CMDS

click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN_EMOJI = True


@click.group(invoke_without_command=True)
@click.option("--version", help="prints the version of program", is_flag=True)
@click.pass_context
def cli(ctx: click.Context, version):
    """
    `honda` is a conda compatible package manager. It is primarily meant for learning and fun.

    Please use `conda` if you actually want to get some work done!
    """
    if version is True:
        click.echo(f'{APP_NAME} {__version__}')
        sys.exit(0)

    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
    ctx.ensure_object(dict)
    ctx.obj["config"] = {}


for cmd in CMDS:
    cli.add_command(cmd)


if __name__ == "__main__":
    cli()
