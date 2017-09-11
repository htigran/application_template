""" Test module to test argument parsing functionality
    of the project
"""

import sys
import unittest2 as unittest
from common.application import Application


def create_application(args):
    """ Create an application instance passing a generated
        config file as a command line argument
    """
    sys.argv = args.split()
    app = Application()
    return app


class ArgumentsTest(unittest.TestCase):
    """ Test suit to contain use cases for testing
        command line argument parsing
    """

    def test_dash_c(self):
        """Test short form of command line argument
        """
        config_file = 'application/config/application.conf'
        app = create_application("test_program -c %s" % config_file)
        self.assertEqual(app.args['config_file'], config_file)

    def test_dash_dash_config_dash_file(self):
        """Test long form of command line argument
        """
        config_file = 'application/config/application.conf'
        app = create_application("test_program --config-file %s" % config_file)
        self.assertEqual(app.args['config_file'], config_file)
