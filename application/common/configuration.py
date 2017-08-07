"""A genneric application configuration reading class
"""
from ConfigParser import RawConfigParser

class Configuration(object): # pylint: disable=too-few-public-methods
    """ Encapsulates configuration related functionality.
    """

    def __init__(self, config_file):
        parser = RawConfigParser()
        parser.read(config_file)

        self.parse(parser)


    def parse(self, parser):
        """
        parses configuration from given parser and updates self with
        the config items and their values
        :param parser: parser to get data from
        :return: None
        """
        config = {}
        for section in parser.sections():
            config[section] = {}
            for key, val in parser.items(section):
                config[section][key] = val

        self.__dict__.update(config)
