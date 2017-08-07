from common.application import Application

class MyApp(Application):

    def __init__(self):
        super(MyApp, self).__init__()

    def run(self):

        print("\n### Application arguments ###\n")
        print(vars(self.args))

        print("\n### Application configuration ###\n")
        print(vars(self.config))


if __name__ == "__main__":
    app = MyApp()
    app.run()
