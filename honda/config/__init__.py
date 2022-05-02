"""
Within this module is everything that reads in application configuration.

This configuration is read in via configuration files and environment variables.
In most cases, environment variables will override values in config files, and
config files will be read from in a priority based order. System level config files (e.g. '/etc/conda/condarc')
are the lowest priority and user config (e.g. '/home/user/.condarc') are the highest
priority.

"""
