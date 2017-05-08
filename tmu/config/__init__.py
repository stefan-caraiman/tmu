import os

from oslo_config import cfg
from oslo_log import log as logging

from tmu.config import factory
from tmu import version

CONFIG = cfg.ConfigOpts()

logging.register_options(CONFIG)
for option_class in factory.get_options():
    option_class(CONFIG).register()

_DEFAULT_CONFIG_FILES = [
    config_file for config_file in ("tmu.conf", "etc/tmu/tmu.conf")
    if os.path.isfile(config_file)
]

if _DEFAULT_CONFIG_FILES:
    CONFIG([], project='tmu', version=version.get_version(),
           default_config_files=_DEFAULT_CONFIG_FILES)
