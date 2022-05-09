"""
Module that holds the cache service for our application
"""
import asyncio
import time
from pathlib import Path
from typing import Sequence, Callable
from urllib import parse

import appdirs

from honda import http

from honda.cli.display.managers import DisplayManager


def get_cache_dir() -> Path:
    """
    Determine a users operating system and return the best location to store cached files
    """
    cache_dir = Path(appdirs.user_cache_dir('honda'))

    # If it doesn't exist, let's create it
    if not cache_dir.exists():
        cache_dir.mkdir(parents=True, exist_ok=True)

    return cache_dir


def get_cache_filename_from_channel_url(channel_url: str) -> Path:
    """
    From a channel url str, return a Path object to location where the cache file is supposed to be.
    """
    url = parse.urlparse(channel_url)
    hostname = f"{url.hostname}-" if url.hostname else ""
    pathname = url.path.lstrip("/").replace("/", "-")
    filename_str = f"{hostname}{pathname}"

    return Path(filename_str)


CACHE_EXPIRY_HOUR = 3600
CACHE_EXPIRY_MINUTE = 60


def get_expired_files(
    files: Sequence[Path], cache_expiry: int = CACHE_EXPIRY_HOUR
) -> Sequence[Path]:
    """
    Checks to see if the supplied files have passed their cache expiry.

    This can happen when:
        - The file doesn't exist
        - The file is past its expiry
    """
    now = time.time()
    return tuple(
        file
        for file in files
        if not file.exists() or file.lstat().st_mtime + cache_expiry <= now
    )


def cache_channel_repodata(
    repodata_urls: Sequence[str],
    display_ctx_manager: Callable[..., DisplayManager],
):
    async def main():
        cache_dir = get_cache_dir()
        await http.limited_download(
            repodata_urls, cache_dir, display_ctx_manager=display_ctx_manager
        )

    asyncio.run(main())
