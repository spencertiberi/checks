from check50 import *


class Credit(Checks):

    @check()
    def exists(self):
        """calc.py exists."""
        self.require("calc.py")

    @check("exists")
    def test1(self):
        """input of 2, +, and 2 yields 4.0"""
        self.spawn("python calc.py").stdin("2")\
		.stdin("+")\
		.stdin("2").stdout("4.0\n", "4.0\n").exit(0)
