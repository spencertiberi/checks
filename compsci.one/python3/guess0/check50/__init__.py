import re

from check50 import *

class Guess0(Checks):

    @check()
    def exists(self):
        """guess0.py exists."""
        self.require("eff.py")

    @check("exists")
    def test1(self):
        """Prints Too low! with input 17"""
        self.spawn("python guess0.py").stdin("17").stdout("Too low!\n").exit(0)

    @check("exists")
    def test2(self):
        """Prints Too high! with input 61"""
        self.spawn("python guess0.py").stdin("61").stdout("Too high!\n").exit(0)

    @check("exists")
    def test3(self):
        """Prints You got it! with input 37"""
        self.spawn("python guess0.py").stdin("37").stdout("You got it!\n").exit(0)
