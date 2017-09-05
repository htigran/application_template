"""
This is a sample application
"""

from pprint import pprint as pp
from common.application import Application


class MyApp(Application):
    """
    This sample class derives from generic Application and gets automatic
    command line arguments handling and configuratoin file hadling
    """

    def test_logger(self):
        """ Simple logger test
        """
        self.logger.info("INFO: bla bla")
        self.logger.warning("WARNING: bla bla")
        self.logger.error("ERROR: bla bla")
        self.logger.critical("CRITICAL: bla bla")
        self.logger.exception("EXCEPTION: bla bla")

    def run(self):
        """ Run the application
        """

        print "\n### Application arguments ###\n"
        pp(self.args)

        print "\n### Application configuration ###\n"
        pp(self.config)

        self.test_logger()


if __name__ == "__main__":
    APP = MyApp()
    APP.run()
