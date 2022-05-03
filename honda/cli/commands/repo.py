"""
This is a command that grabs the latest repo and caches it.
"""
import asyncio
from pathlib import Path

from rich import print as rprint

from honda import cache
from honda.config.main import CONFIG
from honda.http import limited_download
from honda.cli.display.managers import progress_ctx_manager


async def main(download_folder: Path) -> None:
    """main async routine for this command"""
    await limited_download(
        CONFIG.channel_repodata_urls,
        download_folder,
        display_ctx_manager=progress_ctx_manager,
    )


def repo(channel) -> None:
    """
    This command is very similar to the `apt update` command found on Debian systems.

    In order to give a better user experience, we cache all of the repo data
    that is available for the users computer.
    """
    cache_dir = cache.get_cache_dir(CONFIG.env_config.platform, CONFIG.env_config.home)
    rprint("[green italic]Updating channel repo data...")
    asyncio.run(main(cache_dir))
