"""A genneric application argument parsing class
"""
import argparse


def define_arguments(parser):
    """ Define command line arguments
    """
    parser.add_argument("-c",
                        "--config-file",
                        type=str,
                        action="store",
                        required=True,
                        help="path to config file")


def argument_parser():
    """ Parses command line arguments

        :returns a map of argument name:values
    """
    parser = argparse.ArgumentParser()
    define_arguments(parser)
    args = parser.parse_args()
    return vars(args)
