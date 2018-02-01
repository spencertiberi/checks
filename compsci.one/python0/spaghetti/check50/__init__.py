import json
import os
import shlex

from check50 import *


class Spaghetti(Checks):

    @check()
    def exists(self):
        """spaghetti.py exists."""
        self.require("spaghetti.py")

    @check("exists")
    def test1(self):
        """There's vomit on his sweater already!"""
        self.spawn("python spaghetti.py").stdout("There's vomit on his sweater already\nMom's spaghetti").exit(0)
