from __future__ import print_function

from oslo_log import log as logging
import prettytable

from tmu.cli import base as cli_base


LOG = logging.getLogger(__name__)


class _AddTenant(cli_base.Command):

    """Add a new Tenant."""

    def setup(self):
        """Extend the parser configuration in order to expose this command."""
        parser = self._parser.add_parser(
            "add", help="Add a new tenant.")
        parser.add_argument(
            "--name", dest="name", required=True,
            help="The name of the tenant.")
        parser.add_argument(
            "--description", dest="description", required=True,
            help="More information regarding the new tenant.")
        parser.set_defaults(work=self.run)

    def _work(self):
        """Add a new API client."""
        pass


class Tenant(cli_base.Group):

    """Group for all the available user actions."""

    commands = [
        (_AddTenant, "actions"),
    ]

    def setup(self):
        """Extend the parser configuration in order to expose this command."""
        parser = self._parser.add_parser(
            "tenant", help="Operations related to users management.")

        actions = parser.add_subparsers()
        self._register_parser("actions", actions)
