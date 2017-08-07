
from arguments import Arguments
from configuration import Configuration


class Application(object):

    def __init__(self):
        self.args = Arguments()
        self.config = Configuration(self.args.config_file)
