from check50 import *

class Schedule(Checks):

    @check()
    def exists(self):
        """schedule.py exists."""
        self.require("schedule.py")

    @check("exists")
    def test1(self):
        """Input of Friday, 10, and 30 yields yes"""
        self.spawn("python schedule.py").stdin("Friday")\
		.stdin("10")\
        .stdin("30").stdout("yes\n").exit(0)

    @check("exists")
    def test2(self):
        """Input of Sunday, 12, and 30 yields no"""
        self.spawn("python schedule.py").stdin("Sunday")\
		.stdin("12")\
        .stdin("30").stdout("no\n").exit(0)

    @check("exists")
    def test3(self):
        """Input of Monday, 20, and 45 yields no"""
        self.spawn("python schedule.py").stdin("Monday")\
		.stdin("20")\
        .stdin("45").stdout("no\n").exit(0)
