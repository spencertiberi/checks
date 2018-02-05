import re

from check50 import *

class Eff(Checks):

    @check()
    def exists(self):
        """eff.py exists."""
        self.require("eff.py")

    @check("exists")
    def test1(self):
        """Result of 32.895 with input of .45, 21.1, 5.3, 7.1"""
        self.spawn("python eff.py").stdin(".45")\
        .stdin("21.1")\
        .stdin("5.3")\
        .stdin("7.1").stdout("This player's efficiency rating is 32.895!\n").exit(0)
