from check50 import *

class Op(Checks):

    @check()
    def exists(self):
        """operators.py exists."""
        self.require("operators.py")

    @check("exists")
    def test1(self):
        """Input of 7 and 2"""
        self.spawn("python operators.py").stdin("7")\
		.stdin("2").stdout("Sum: 9\nDifference: 5\nProduct: 14\nQuotient: 3.5\nRemainder: 1").exit(0)

    @check("exists")
    def test2(self):
        """Input of 5 and 4"""
        self.spawn("python operators.py").stdin("7")\
		.stdin("4").stdout("Sum: 11\nDifference: 3\nProduct: 28\nQuotient: 1.75\nRemainder: 3").exit(0)
