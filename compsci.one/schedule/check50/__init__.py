from check50 import *


class Schedule(Checks):

    @check()
    def exists(self):
        """schedule.py exists."""
        self.require("schedule.py")

    @check("exists")
    def test1(self):
        """time of 10:30 on Friday yields yes"""
        self.spawn("python schedule.py").stdin("Friday")\
		.stdin("10")\
		.stdin("30").stdout("yes\n", "yes\n").exit(0)

    @check("exists")
    def test2(self):
        """time of 17:30 on Monday yields no"""
        self.spawn("python schedule.py").stdin("Friday")\
		.stdin("17")\
		.stdin("30").stdout("no\n", "no\n").exit(0)

    @check("exists")
    def test3(self):
        """Sunday yields no"""
        self.spawn("python schedule.py").stdin("Sunday")\
		.stdin("12")\
		.stdin("30").stdout("no\n", "no\n").exit(0)
