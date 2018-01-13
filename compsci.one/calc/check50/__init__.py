from check50 import *


class Credit(Checks):

    @check()
    def exists(self):
        """calc.py exists."""
        self.require("calc.py")

    @check("exists")
    def test1(self):
        """input of 2, +, and 4 yields 6.0"""
        self.spawn("python calc.py").stdin("2")\
		.stdin("+")\
		.stdin("4").stdout("6.0\n", "6.0\n").exit(0)

    @check("exists")
    def test2(self):
        """input of 2, -, and 4 yields -2.0"""
        self.spawn("python calc.py").stdin("2")\
		.stdin("-")\
		.stdin("4").stdout("-2.0\n", "-2.0\n").exit(0)

    @check("exists")
    def test3(self):
        """input of 2, x, and 4 yields 8.0"""
        self.spawn("python calc.py").stdin("2")\
		.stdin("x")\
		.stdin("4").stdout("8.0\n", "8.0\n").exit(0)

    @check("exists")
    def test4(self):
        """input of 2, /, and 4 yields 0.5"""
        self.spawn("python calc.py").stdin("2")\
		.stdin("/")\
		.stdin("4").stdout("0.5\n", "0.5\n").exit(0)

    @check("exists")
    def test5(self):
        """input of 2, ^, and 4 yields 16.0"""
        self.spawn("python calc.py").stdin("2")\
		.stdin("^")\
		.stdin("4").stdout("16.0\n", "16.0\n").exit(0)

    @check("exists")
    def test6(self):
        """informs user of "invalid opperation""""
        self.spawn("python calc.py").stdin("2")\
		.stdin("&")\
		.stdin("4").stdout("^invalid\sopperation\n", "invalid opperation\n").exit(0)
