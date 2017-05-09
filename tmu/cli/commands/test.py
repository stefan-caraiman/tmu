
from oslo_log import log as logging
import prettytable

from tmu.cli import base as cli_base


LOG = logging.getLogger(__name__)


class _RunTest(cli_base.Command):

    """Run test for a tenant."""

    def setup(self):
        """Extend the parser configuration in order to expose this command."""
        parser = self._parser.add_parser(
            "test", help="Run tests on a tenant.")
        parser.add_argument(
            "--name", dest="name", required=True,
            help="The name of the tenant to be tested.")
        parser.add_argument(
            "--test-name", dest="test_name", required=True,
            help="Name of the test scenario to be run")
        parser.set_defaults(work=self.run)

    def _work(self):
        """Add the test logic."""
        pass


class TestTenant(cli_base.Group):

    """Group for all the available user actions."""

    commands = [
        (_RunTest, "actions"),
    ]

    def setup(self):
        """Extend the parser configuration in order to expose this command."""
        parser = self._parser.add_parser(
            "test", help="Operations related to testing the application.")

        actions = parser.add_subparsers()
        self._register_parser("actions", actions)
