#!/usr/bin/env python
""" Test the application logger
"""
import mock
import unittest2 as unittest
from testfixtures import LogCapture
from test_configuration import create_application


class TestLogger(unittest.TestCase):
    """ Logging test suit
    """

    def test_debug(self):
        """ test debug log level
            1) application is created with log level 'debug'
            2) write a debug text in logger and verify that the logger has
               been called with the text
        """

        app = create_application(log_level=1)
        with mock.patch.object(app.logger, 'debug') as log_debug_mock:
            app.logger.debug('DEADBEEF')
            log_debug_mock.assert_called_with('DEADBEEF')

    def test_info(self):
        """ test info log level
            1) application is created with log level 'info'
            2) write a debug text in the logger and verify that the logger has
               not been called
            3) write a info text in the logger and verify that the logger has
               been called with the text
        """
        app = create_application(log_level=2)
        with LogCapture() as log:
            app.logger.debug('DEADBEEF')
            log.check()

        with mock.patch.object(app.logger, 'info') as log_info_mock:
            app.logger.info('DEADBEEF')
            log_info_mock.assert_called_with('DEADBEEF')

    def test_warning(self):
        """ test warning log level
            1) application is created with log level 'warning'
            2) write a info text in the logger and verify that the logger has
               not been called
            3) write a warning text in the logger and verify that the logger
               has been called with the text
        """
        app = create_application(log_level=3)
        with LogCapture() as log:
            app.logger.info('DEADBEEF')
            log.check()

        with mock.patch.object(app.logger, 'warning') as log_warning_mock:
            app.logger.warning('DEADBEEF')
            log_warning_mock.assert_called_with('DEADBEEF')

    def test_error(self):
        """ test info log level
            1) application is created with log level 'error'
            2) write a warning text in the logger and verify that the logger
               has not been called
            3) write a error text in the logger and verify that the logger has
               been called with the text
        """
        app = create_application(log_level=4)
        with LogCapture() as log:
            app.logger.warning('DEADBEEF')
            log.check()

        with mock.patch.object(app.logger, 'error') as log_error_mock:
            app.logger.error('DEADBEEF')
            log_error_mock.assert_called_with('DEADBEEF')

    def test_critical(self):
        """ test info log level
            1) application is created with log level 'critical'
            2) write an error text in the logger and verify that the logger
               has not been called
            3) write a critical text in the logger and verify that the logger
               has been called with the text
        """
        app = create_application(log_level=5)
        with LogCapture() as log:
            app.logger.error('DEADBEEF')
            log.check()

        with mock.patch.object(app.logger, 'critical') as log_critical_mock:
            app.logger.critical('DEADBEEF')
            log_critical_mock.assert_called_with('DEADBEEF')
