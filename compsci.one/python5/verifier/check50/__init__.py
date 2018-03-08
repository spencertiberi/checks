from check50 import *


class verifier(Checks):

    @check()
    def exists(self):
        """verifier.py exists."""
        self.require("verifier.py")

    @check("exists")
    def test1(self):
        """2 + 2 equals 4 returns Correct!"""
        self.spawn("python verifier.py").stdin("2")\
        .stdin("2")\
		.stdin("4").stdout("Correct!\n").exit(0)

    @check("exists")
    def test2(self):
        """2 + 6 equals 4 returns Inorrect!"""
        self.spawn("python verifier.py").stdin("2")\
        .stdin("6")\
		.stdin("4").stdout("Incorrect!\n").exit(0)
