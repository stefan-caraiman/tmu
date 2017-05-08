"""Config options available for the TMU setup."""

from oslo_config import cfg

from tmu.config import base as conf_base


class TMUOptions(conf_base.Options):

    """Config options available for the tmu setup."""

    def __init__(self, config):
        super(TMUOptions, self).__init__(config, group="DEFAULT")
        self._options = [
            cfg.StrOpt(
                "tenant_name", default="", required=True,
                help="The name of the tenant that will be tested, "
                     "created or updated"),
        ]

    def register(self):
        """Register the current options to the global ConfigOpts object."""
        group = cfg.OptGroup(self.group_name, title='TMU Options')
        self._config.register_group(group)
        self._config.register_opts(self._options, group=group)

    def list(self):
        """Return a list which contains all the available options."""
        return self._options
