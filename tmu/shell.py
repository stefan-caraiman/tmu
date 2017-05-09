"""This module contains the entry point for the command line application."""

import argparse
import sys

from oslo_log import log as logging

from tmu.cli import base as cli_base
from tmu.cli import commands as cli_commands
from tmu import config

CONFIG = config.CONFIG


class TmuCli(cli_base.Application):

    """Command line application for interacting with TmuCli."""

    commands = [
        (cli_commands.Tenant, "commands"),
        (cli_commands.TestTenant, "commands")
    ]

    def setup(self):
        """Setup the command line parser.
        Extend the parser configuration in order to expose all
        the received commands.
        """
        self._parser = argparse.ArgumentParser()
        commands = self._parser.add_subparsers(title="[commands]",
                                               dest="command")

        self._register_parser("commands", commands)


def main():
    """The TMU command line application."""
    logging.setup(CONFIG, "tmu")
    tmu = TmuCli(sys.argv[1:])
    tmu.run()
    return tmu.result
