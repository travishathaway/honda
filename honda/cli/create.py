import asyncio
from pathlib import Path

from rich import print as rprint

from honda.config.main import CONFIG
from honda.http import limited_download
from honda.cli.display.managers import ProgressCtxManager


async def main(folder: Path) -> None:
    await limited_download(
        CONFIG.channel_repodata_urls, folder, display_ctx_manager=ProgressCtxManager
    )


def create(folder, test):
    rprint("[green italic]Updating repodata...")
    # asyncio.run(main(Path(folder)))
