from check50 import *

class Truth(Checks):

    @check()
    def exists(self):
        """truth.py exists."""
        self.require("truth.py")

    @check("exists")
    def test1(self):
        """Input of true and false"""
        self.spawn("python truth.py").stdin("true")\
		.stdin("false").stdout("A and B: false\nA or B: true\nNot A: false\nNot B: true\n").exit(0)

    @check("exists")
    def test2(self):
        """Input of true and true"""
        self.spawn("python truth.py").stdin("true")\
		.stdin("true").stdout("A and B: true\nA or B: true\nNot A: false\nNot B: false\n").exit(0)

    @check("exists")
    def test3(self):
        """Input of false and false"""
        self.spawn("python truth.py").stdin("false")\
		.stdin("false").stdout("A and B: false\nA or B: false\nNot A: true\nNot B: true\n").exit(0)
