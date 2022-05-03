import os
import platform
from pathlib import Path
from typing import Optional, Sequence
from urllib import parse

from honda import cache
from honda.config.condarc import CondarcConfig, get_condarc_obj
from honda.config.env import EnvironmentConfig
from honda.config import constants as const
from honda.types.channel import Channel


class Config:
    """
    Main configuration object for the entire application

    Properties are lazy loaded, so they are parse until they are
    accessed in the program.
    """

    __slots__ = ("__env_config", "__condarc")

    def __init__(
        self,
        env_config: Optional[EnvironmentConfig] = None,
        condarc: Optional[CondarcConfig] = None,
    ):
        self.__env_config = env_config
        self.__condarc = condarc

    @property
    def env_config(self) -> EnvironmentConfig:
        if self.__env_config is None:
            self.__env_config = EnvironmentConfig()

        return self.__env_config

    @property
    def condarc(self) -> CondarcConfig:
        if self.__condarc is None:
            self.__condarc = get_condarc_obj(self.env_config.valid_condarc_files)

        return self.__condarc

    @property
    def subdirs(self) -> Sequence[str]:
        """
        Returns applicable subdirs for the computer's operation system (e.g. 'linux-64', 'noarch')
        """
        subdirs = (
            get_sys_subdir(),
            "noarch",
        )
        return subdirs

    @property
    def channels(self) -> Sequence[Channel]:
        """Returns channels as channel objcts"""
        # TODO: add in channels from CLI parameters
        return tuple(Channel(url=channel) for channel in self.condarc.channels)

    @property
    def channel_urls(self) -> Sequence[str]:
        """Returns all the channel URLs that are currently active"""
        channels = []
        if (
            const.DEFAULTS_CHANNEL_NAME in self.condarc.channels
        ):  # TODO: this needs to account for CLI args too
            channels += [
                f"{parse.urljoin(channel, subdir)}/"
                for channel in self.env_config.default_channels
                for subdir in self.subdirs
            ]

        other_channels = set(self.condarc.channels) - const.DEFAULTS_CHANNEL_ALIASES
        channels += [
            f"{parse.urljoin(const.DEFAULT_CHANNEL_ALIAS, os.path.join(chnl, subdir))}/"
            for chnl in other_channels
            for subdir in self.subdirs
        ]

        return channels

    @property
    def channel_repodata_urls(self) -> Sequence[str]:
        return tuple(parse.urljoin(url, "repodata.json") for url in self.channel_urls)

    @property
    def channel_repodata_cache_files(self) -> Sequence[Path]:
        """Returns what the filenames for the repo data should be"""
        cache_dir = cache.get_cache_dir(self.env_config.platform, self.env_config.home)
        return tuple(
            cache_dir.joinpath(cache.get_cache_filename_from_channel_url(url))
            for url in self.channel_repodata_urls
        )


CONFIG = Config()


__ARCH_MAP = {"x86_64": "64", "x86": "32"}


def get_sys_subdir() -> str:
    mach = platform.machine()
    system = platform.system().lower()
    mach_num = __ARCH_MAP.get(mach)

    return f"{system}-{mach_num}"
