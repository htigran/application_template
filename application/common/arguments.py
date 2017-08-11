"""A genneric application argument parsing class
"""
import argparse


class Arguments(object):
    """ Encapsulates argumet parsing related functionality.
    """

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-c",
                            "--config-file",
                            type=str,
                            action="store",
                            required=True,
                            help="path to config file")

        args = parser.parse_args()
        self.__dict__.update(vars(args))
