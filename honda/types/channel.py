from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from honda import cache


@dataclass(slots=True)
class Channel:
    """
    Represents a channel which can come in a couple different varieties:

    - Name (e.g. "defaults", "bioconda", "conda-forge")
    - File path (e.g. "/home/user/channel_dir")
    - URL (e.g. "https://honda.com/pkgs")
    """

    url: Optional[str] = field(default=None)
    """
    Channel url which can either point at a http/s resource or a file resource.

    Examples:
        - file:///home/user/channel_dir
        - https://honda.com/pkgs
    """

    repodata_cache: Optional[Path] = field(default=None)
    """
    Path to the channel's `repodata.json` cache file

    Examples:
        - /home/user/.cache/honda/repo.anaconda.com-pkgs-main-noarch-repodata.json
    """

    name: Optional[str] = field(default=None)
    """
    Name of the channel.

    Examples:
        - conda-forge
        - defaults
    """

    platform: Optional[str] = field(default=None)
    """
    Platform the user is running which comes from the `platform` module
    """

    home: Optional[str] = field(default=None)
    """
    User's HOME folder
    """

    def __post_init__(self, *_, **kwargs):
        if not kwargs.get("repodata_cache"):
            self.__set_repodata_cache()

    def __set_repodata_cache(self):
        cache_dir = cache.get_cache_dir(self.platform, self.home)
        self.repodata_cache = cache_dir.joinpath(
            cache.get_cache_filename_from_channel_url(self.url)
        )
