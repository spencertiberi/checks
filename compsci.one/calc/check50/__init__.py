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

    @check("exists")
    def test2(self):
        """input of 2, -, and 2 yields 0.0"""
        self.spawn("python calc.py").stdin("2")\
		.stdin("-")\
		.stdin("2").stdout("0.0\n", "0.0\n").exit(0)

    @check("exists")
    def test3(self):
        """input of 2, x, and 2 yields 4.0"""
        self.spawn("python calc.py").stdin("2")\
		.stdin("x")\
		.stdin("2").stdout("4.0\n", "4.0\n").exit(0)
