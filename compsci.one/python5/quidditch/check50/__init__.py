from check50 import *


class quidditch(Checks):

    @check()
    def exists(self):
        """quidditch.py exists."""
        self.require("quidditch.py")

    @check("exists")
    def test1(self):
        """input of 5 and 1 yields 200"""
        self.spawn("python quidditch.py").stdin("5")\
		.stdin("1").stdout("Your team's final score is: 200\n").exit(0)

    @check("exists")
    def test2(self):
        """input of 3 and 0 yields 30"""
        self.spawn("python quidditch.py").stdin("3")\
		.stdin("0").stdout("Your team's final score is: 30\n").exit(0)
