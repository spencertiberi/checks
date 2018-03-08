from check50 import *


class maximum(Checks):

    @check()
    def exists(self):
        """maximum.py exists."""
        self.require("maximum.py")

    @check("exists")
    def test1(self):
        """finds max in [1,2,3,4,5]"""
        self.spawn("python maximum.py").stdin("1")\
		.stdin("2")\
        .stdin("3")\
        .stdin("4")\
        .stdin("5").stdout("Maximum: 5\n").exit(0)

    @check("exists")
    def test2(self):
        """finds max in [5,4,3,2,1]"""
        self.spawn("python maximum.py").stdin("5")\
		.stdin("4")\
        .stdin("3")\
        .stdin("2")\
        .stdin("1").stdout("Maximum: 5\n").exit(0)

    @check("exists")
    def test3(self):
        """finds max in [8,11,27,17,-5]"""
        self.spawn("python maximum.py").stdin("8")\
		.stdin("11")\
        .stdin("27")\
        .stdin("17")\
        .stdin("-5").stdout("Maximum: 27\n").exit(0)
