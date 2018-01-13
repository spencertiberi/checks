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
        """input of 2, x, and 3 yields 6.0"""
        self.spawn("python calc.py").stdin("2")\
		.stdin("x")\
		.stdin("3").stdout("6.0\n", "6.0\n").exit(0)

    @check("exists")
    def test4(self):
        """input of 4, /, and 2 yields 2.0"""
        self.spawn("python calc.py").stdin("4")\
		.stdin("/")\
		.stdin("2").stdout("2.0\n", "2.0\n").exit(0)

    @check("exists")
    def test5(self):
        """input of 3, ^, and 2 yields 9.0"""
        self.spawn("python calc.py").stdin("3")\
		.stdin("^")\
		.stdin("2").stdout("9.0\n", "9.0\n").exit(0)
