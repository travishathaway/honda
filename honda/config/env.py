import os
import sys
from dataclasses import dataclass, field
from pathlib import Path
import platform
from typing import Sequence

from honda.config import constants as const


@dataclass(slots=True)
class EnvironmentConfig:
    """
    This is the main configuration object. It stores all configuration
    for the program. This configuration comes from a mix of environment
    variables and config files.
    """

    #: Search path which determines where we find multiple `condarc` confiugrations
    search_path: Sequence[str] = field(default=None)

    #: Users HOME directory
    home: str = field(default="")

    #: Users PATH variable
    path: str = field(default="")

    #: Shell the user is current running
    shell: str = field(default="")

    #: Determines whether we are running on Windows or not
    is_windows: bool = field(default=False)

    #: Full path to your base conda install (not sure this is actually used)
    conda_root: str = field(default="")

    #: Full path to the current active environment
    conda_prefix: str = field(default="")

    #: Path to the currently configured conda executable
    conda_exe: str = field(default="")

    #: Path to the currently configured conda python executable
    conda_python_exe: str = field(default="")

    #: Path to the currently configured conda python executable
    conda_shlvl: int = field(default=1)

    #: Name of the default environment (currently activated one)
    conda_default_env: int = field(default="")

    #: Override and point to a specific condarc file
    condarc: str = field(default="")

    #: ???? Not sure about this one
    xdg_config_home: str = field(default="")

    #: Default path user's .condarc file
    user_rc_path: Path = field(
        default=Path(os.path.abspath(os.path.expanduser("~/.condarc")))
    )

    #: Default path for system .condarc file
    sys_rc_path: Path = field(default=Path(os.path.join(sys.prefix, ".condarc")))

    def __post_init__(self, *_, **kwargs):
        """
        This method sets the default values for our properties. These mostly
        come from the environment and can be overridden.
        """
        # Set all the environment variables we care about
        self.home = kwargs.get("home") or os.getenv("HOME", "")
        self.path = kwargs.get("path") or os.getenv("PATH", "")
        self.shell = kwargs.get("shell") or os.getenv("SHELL", "")
        self.conda_root = kwargs.get("conda_root") or os.getenv("CONDA_ROOT", "")
        self.conda_prefix = kwargs.get("conda_prefix") or os.getenv("CONDA_PREFIX", "")
        self.conda_exe = kwargs.get("conda_exe") or os.getenv("CONDA_EXE", "")
        self.conda_python_exe = kwargs.get("conda_python_exe") or os.getenv(
            "CONDA_PYTHON_EXE", ""
        )
        self.conda_shlvl = kwargs.get("conda_shlvl") or os.getenv("CONDA_SHLVL", "")
        self.conda_default_env = kwargs.get("conda_default_env") or os.getenv(
            "CONDA_DEFAULT_ENV", ""
        )
        self.condarc = kwargs.get("condarc") or os.getenv("CONDARC", "")
        self.xdg_config_home = kwargs.get("xdg_config_home") or os.getenv(
            "XDG_CONFIG_HOME", ""
        )

        # Determine OS type
        self.is_windows = kwargs.get("is_windows") or (
            sys.platform.startswith("win")
            or (sys.platform == "cli" and os.name == "nt")
        )

        # Setup search path for parsing condarc config files
        self.search_path = kwargs.get("search_path") or get_search_path_from_config(
            self
        )

    @property
    def valid_condarc_files(self) -> Sequence[Path]:
        """
        Using the search_path property, return a list of condarc files which actually exist"

        TODO: maybe cache this? This environment config is mutable, but I don't expect consumers
              to change anything after __post_init__ has run.
        """
        return tuple(
            Path(path_str)
            for path_str in self.search_path
            if os.path.exists(path_str) and os.path.isfile(path_str)
        )

    @property
    def default_channels(self) -> Sequence[str]:
        """We differ the default channels that configured depending on OS type"""
        return (
            const.DEFAULT_CHANNELS_WIN
            if self.is_windows
            else const.DEFAULT_CHANNELS_UNIX
        )

    @property
    def compatible_shells(self) -> Sequence[str]:
        """Depending on which OS is currently configured, we'll want to display different shells"""
        return (
            const.COMPATIBLE_SHELLS_WIN
            if self.is_windows
            else const.COMPATIBLE_SHELLS_NIX
        )

    @property
    def platform(self) -> str:
        """Grab the platform we are using (wrapper around platform module)"""
        return platform.system().lower()


def get_search_path_from_config(config: EnvironmentConfig) -> Sequence[str]:
    """
    Uses config parameters to determine the search path.
    """
    if config.is_windows:
        search_path = (
            "C:/ProgramData/conda/.condarc",
            "C:/ProgramData/conda/condarc",
            "C:/ProgramData/conda/condarc.d",
        )
    else:
        search_path = (
            "/etc/conda/.condarc",
            "/etc/conda/condarc",
            "/etc/conda/condarc.d/",
            "/var/lib/conda/.condarc",
            "/var/lib/conda/condarc",
            "/var/lib/conda/condarc.d/",
        )

    if config.conda_root:
        search_path += (
            f"{config.conda_root}/.condarc",
            f"{config.conda_root}/condarc",
            f"{config.conda_root}/condarc.d/",
        )

    if config.xdg_config_home:
        search_path += (
            f"{config.xdg_config_home}/.condarc",
            f"{config.xdg_config_home}/condarc",
            f"{config.xdg_config_home}/condarc.d/",
        )

    if config.conda_prefix:
        search_path += (
            f"{config.conda_prefix}/.condarc",
            f"{config.conda_prefix}/condarc",
            f"{config.conda_prefix}/condarc.d/",
            f"{config.condarc}",
        )

    search_path += (
        f"{config.home}/.config/conda/.condarc",
        f"{config.home}/.config/conda/condarc",
        f"{config.home}/.config/conda/condarc.d/",
        f"{config.home}/.conda/.condarc",
        f"{config.home}/.conda/condarc",
        f"{config.home}/.conda/condarc.d/",
        f"{config.home}/.condarc",
    )

    return search_path
