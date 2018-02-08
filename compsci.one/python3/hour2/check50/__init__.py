from check50 import *

class Hour2(Checks):

    @check()
    def exists(self):
        """hour2.py exists."""
        self.require("hour2.py")

    @check("exists")
    def test1(self):
        """Prints 3 with input of 9 and 6."""
        self.spawn("python hour2.py").stdin("9")\
        .stdin("6").stdout("In 7 hours it will be 3 o'clock\n", "In 5 hours it will be 2 o'clock\n").exit(0)

    @check("exists")
    def test1(self):
        """Prints 12 with input of 5 and 7."""
        self.spawn("python hour2.py").stdin("5")\
        .stdin("7").stdout("In 7 hours it will be 12 o'clock\n", "In 5 hours it will be 2 o'clock\n").exit(0)
