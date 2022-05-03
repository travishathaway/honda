import asyncio
from pathlib import Path

from rich import print as rprint
from rich.pretty import pprint

from honda import cache
from honda.config.main import CONFIG
from honda.http import limited_download
from honda.cli.display.managers import progress_ctx_manager


async def main(folder: Path) -> None:
    await limited_download(
        CONFIG.channel_repodata_urls, folder, display_ctx_manager=progress_ctx_manager
    )


def create(no_cache):
    display_ctx_manager = (
        progress_ctx_manager  # TODO: should be determined by configuration options
    )
    expired = cache.get_expired_files(CONFIG.channel_repodata_cache_files)
    # cache.cache_channel_repodata(
    #     CONFIG.env_config.platform, CONFIG.env_config.home, expired, display_ctx_manager
    # )
    pprint(expired)
    # asyncio.run(main(Path(folder)))
