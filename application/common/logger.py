""" Create loggers
"""

import os
import logging
from logging.handlers import TimedRotatingFileHandler


__log_levels__ = [logging.NOTSET,
                  logging.DEBUG,
                  logging.INFO,
                  logging.WARNING,
                  logging.ERROR,
                  logging.CRITICAL]


def create_timed_rotating_log(logfile,
                              loglevel=2,
                              name=__name__):
    """ Create a timed rotating logger and return the isntance
    """
    logger = logging.getLogger(name)
    level_index = int(loglevel)
    logger.setLevel(__log_levels__[level_index])

    path = os.path.abspath(logfile)
    handler = TimedRotatingFileHandler(path,
                                       when="m",
                                       interval=1,
                                       backupCount=5)
    logger.addHandler(handler)

    return logger
