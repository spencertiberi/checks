from check50 import *

class Eight(Checks):

    @check()
    def exists(self):
        """eight.py exists."""
        self.require("eight.py")

    @check("exists")
    def test1(self):
        """Prints 80 when 10 is entered."""
        self.spawn("python eight.py").stdin("10").stdout("80\n", "80\n").exit(0)
