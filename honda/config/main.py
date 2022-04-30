from dataclasses import dataclass

from honda.config.condarc import CondaRC
from honda.config.env import EnvironmentConfig


def get_app_config() -> 'Config':
    env_config = EnvironmentConfig()
    condarc = CondaRC(env_config=env_config)

    return Config(condarc=condarc, env_config=env_config)


@dataclass(slots=True)
class Config:
    """
    Main configuration object for the entire application
    """
    #: Holds all of the variables contained within condarc file(s)
    condarc: CondaRC

    #: Holds environment specific configuration
    env_config: EnvironmentConfig
