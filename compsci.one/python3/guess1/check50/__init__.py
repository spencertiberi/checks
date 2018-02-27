import re

from check50 import *

class Guess1(Checks):

    @check()
    def exists(self):
        """guess1.py exists."""
        self.require("guess1.py")

    @check("exists")
    def test1(self):
        """Prints Too low! with input 17"""
        self.spawn("python guess1.py").stdin("17").stdout("Too low!\n")

    @check("exists")
    def test2(self):
        """Prints Too high! with input 61"""
        self.spawn("python guess1.py").stdin("61").stdout("Too high!\n")

    @check("exists")
    def test3(self):
        """Prints You got it! with input 37"""
        self.spawn("python guess1.py").stdin("42").stdout("You got it!\n")

    @check("exists")
    def test4(self):
        """Repeats"""
        self.spawn("python guess1.py").stdin("17").stdout("Too low!\n").stdin("42").stdout("You got it!\n")
