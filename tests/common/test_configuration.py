""" Test module to test configuration file parsing part of the project
"""
import sys
import os
import tempfile
import unittest2 as unittest
from common.application import Application


def config_file_generator(log_level):
    """ generates a config file with given arguments
    """

    config_content = "\n".join(["[main]",
                                "user = user",
                                "",
                                "[logger]",
                                "file = logs/test.log",
                                "",
                                "level = {level}".format(level=log_level)])
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(config_content)
        return temp.name


def create_application(log_level=1):
    """ Create an application instance passing a generated
        config file as a command line argument
    """
    config_file = config_file_generator(log_level)
    sys.argv = ['test', '-c', config_file]
    app = Application()
    os.unlink(config_file)
    return app


class ConfigurationTest(unittest.TestCase):
    """  Test suit for testing the config file
         reading and parsing functionality.
    """

    def test_simple(self):
        """ Test simple config file read/parse functionality
        """
        app = create_application()
        self.assertEqual(app.config['main']['user'], 'user')

        self.assertEqual(app.config['logger']['file'], 'logs/test.log')
        self.assertEqual(app.config['logger']['level'], '1')
