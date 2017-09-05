"""A genneric application base class
"""
from common.arguments import argument_parser
from common.configuration import configuration_parser
from common.logger import create_timed_rotating_log


class Application(object):
    """ Parses arguments and reads given by -c/--config-file argument config
    """

    def __init__(self):
        """ Initialize the application
             * Parse command line arguments
             * Parse configuration file
             * Create logger
        """

        # arguments
        self.args = argument_parser()

        # config
        config_file = self.args['config_file']
        self.config = configuration_parser(config_file)

        # logger
        log_file = self.config['logger']['file']
        log_level = self.config['logger']['level']
        self.logger = create_timed_rotating_log(log_file, log_level)
