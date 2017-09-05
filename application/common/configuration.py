"""A genneric application configuration reading class
"""

from ConfigParser import RawConfigParser


def configuration_parser(config_file):
    """
    Parse given configuration file in a map

    :param config_file: configuration file to be parsed

    :return: a map containing configuration sections as keys and configuratino
             items as values

    """
    parser = RawConfigParser()
    parser.read(config_file)

    config = {}
    for section in parser.sections():
        config[section] = {conf: val for conf, val in parser.items(section)}

    return config
