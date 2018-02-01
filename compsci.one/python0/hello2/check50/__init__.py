from check50 import *

class Calc(Checks):

    @check()
    def exists(self):
        """hello2.py exists."""
        self.require("hello2.py")

    @check("exists")
    def test1(self):
        """input of Billy yields \"Hello, Billy!\""""
        self.spawn("python hello2.py").stdin("Billy").stdout("Hello, Billy!\n", "Hello, Billy!\n").exit(0)
