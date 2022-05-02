"""
Module that holds the cache service for our application
"""
import os
from pathlib import Path

from honda.config.main import Config


def get_cache_dir(config: Config) -> Path:
    """
    Determine a users operating system and return the best location to store cached files
    """
    # TODO: design
    if "linux" in config.env_config.platform:
        cache_dir = Path(config.env_config.home).joinpath(".cache/honda/")
    elif "win" in config.env_config.platform:
        cache_dir = Path(os.path.expandvars("%LOCALAPPDATA%\\honda\\"))  # TODO: windows
    elif "darwin" in config.env_config.platform:
        cache_dir = Path(config.env_config.home).joinpath("Library/Caches/honda/")
    else:
        raise NotImplemented(
            "Could not determine operating system type. Only Windows, Linux and OSX are supported."
        )

    # If doesn't exists, let's create it
    if not cache_dir.exists():
        cache_dir.mkdir(parents=True, exist_ok=True)

    return cache_dir
