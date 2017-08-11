"""
This is a sample application
"""

from common.application import Application


class MyApp(Application):
    """
    This sample class derives from generic Application and gets automatic
    command line arguments handling and configuratoin file hadling
    """

    def __init__(self):
        """
        Need to call supers' __init__
        """
        super(MyApp, self).__init__()

    def test_logger(self):
        self.logger.info("INFO: bla bla")
        self.logger.warning("WARNING: bla bla")
        self.logger.error("ERROR: bla bla")
        self.logger.critical("CRITICAL: bla bla")
        self.logger.exception("EXCEPTION: bla bla")

    def run(self):
        """
        Run the application
        """

        print "\n### Application arguments ###\n"
        print vars(self.args)

        print "\n### Application configuration ###\n"
        print vars(self.config)

        self.test_logger()


if __name__ == "__main__":
    APP = MyApp()
    APP.run()
