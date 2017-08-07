"""A genneric application base class
"""
from common.arguments import Arguments
from common.configuration import Configuration


class Application(object): # pylint: disable=too-few-public-methods
    """ Parses arguments and reads given by -c/--config-file argument config file
    """

    def __init__(self):
        self.args = Arguments()
        self.config = Configuration(self.args.config_file) #pylint: disable=maybe-no-member
