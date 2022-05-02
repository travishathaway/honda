import sys

from rich.pretty import pprint

from honda.__version__ import __version__
from honda.config import constants as const
from honda.config.dependencies import app_config
from honda.config.main import Config
from .display.table import print_no_header_table


@app_config
def info(config: Config):
    print_no_header_table(
        const.APP_NAME,
        {
            "active_environment": config.env_config.conda_default_env or "n/a",
            # "active_env_location": config.env_config.conda_prefix or 'n/a',
            "shell_level": config.env_config.conda_shlvl,
            "user_config_file": str(config.env_config.user_rc_path),
            "populated_config_files": tuple(
                str(path) for path in config.env_config.valid_condarc_files
            ),
            "honda_version": __version__,
            "python_version": ".".join(map(str, sys.version_info)),
            "requests_version": "n/a",
            "user-agent": "conda/4.12.0.post41+6a1493bee requests/2.27.1 CPython/3.10.4 Darwin/21.3.0 OSX/12.2.1",
            "channel_urls": config.channel_urls,
            "default_channels": config.env_config.default_channels,
            "subdirs": config.subdirs,
        },
    )

    # pprint(config.env_config)
