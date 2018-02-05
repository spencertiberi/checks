from check50 import *

class hour(Checks):

    @check()
    def exists(self):
        """hour.py exists."""
        self.require("hour.py")

    @check("exists")
    def test1(self):
        """Prints 2 with input of 9."""
        self.spawn("python hour.py").stdin("9").stdout("In 5 hours it will be 2 o'clock\n", "In 5 hours it will be 2 o'clock\n").exit(0)

    @check("exists")
    def test2(self):
        """Prints 11 with input of 6."""
        self.spawn("python hour.py").stdin("6").stdout("In 5 hours it will be 11 o'clock\n", "In 5 hours it will be 11 o'clock\n").exit(0)
