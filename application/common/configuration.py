
from ConfigParser import RawConfigParser

class Configuration():

    def __init__(self, config_file):
        parser = RawConfigParser()
        parser.read(config_file)

        configs = self.parse(parser)
        self.__dict__.update(configs)

    def parse(self, parser):
        config = {}
        for section in parser.sections():
            config[section] = {}
            for key, val in parser.items(section):
                config[section][key] = val

        return config