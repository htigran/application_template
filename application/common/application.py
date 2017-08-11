"""A genneric application base class
"""
import os
import logging
from logging.handlers import TimedRotatingFileHandler

from common.arguments import Arguments
from common.configuration import Configuration


class Application(object):
    """ Parses arguments and reads given by -c/--config-file argument config
    """

    def __init__(self):
        """
        """
        self.args = Arguments()
        config = self.args.config_file
        self.config = Configuration(config)
        self.logger = self.create_timed_rotating_log()

    def create_timed_rotating_log(self):
        """ Create a timed rotating logger and return the isntance
        """
        logger = logging.getLogger("Rotating Log")
        levels = [logging.NOTSET, logging.DEBUG, logging.INFO, logging.WARNING,
                  logging.ERROR, logging.CRITICAL]
        level_index = int(self.config.logger['level'])
        logger.setLevel(levels[level_index])

        path = os.path.abspath(self.config.logger['file'])
        handler = TimedRotatingFileHandler(path,
                                           when="m",
                                           interval=1,
                                           backupCount=5)
        logger.addHandler(handler)

        return logger
