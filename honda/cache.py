"""
Module that holds the cache service for our application
"""
import os
import time
from pathlib import Path
from urllib import parse
from typing import Sequence


def get_cache_dir(platform: str, home_dir: str) -> Path:
    """
    Determine a users operating system and return the best location to store cached files
    """
    # TODO: design
    if "linux" in platform:
        cache_dir = Path(home_dir).joinpath(".cache/honda/")
    elif "win" in platform:
        cache_dir = Path(os.path.expandvars("%LOCALAPPDATA%\\honda\\"))  # TODO: windows
    elif "darwin" in platform:
        cache_dir = Path(home_dir).joinpath("Library/Caches/honda/")
    else:
        raise NotImplemented(
            "Could not determine operating system type. Only Windows, Linux and OSX are supported."
        )

    # If doesn't exists, let's create it
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
    Checks to see if the supplied files have passed their cache expiry
    """
    now = time.time()
    return tuple(file for file in files if file.lstat().st_mtime + cache_expiry <= now)
