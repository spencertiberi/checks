import re

from check50 import *

class Exists(Checks):

    @check()
    def exists(self):
        """quad.py exists."""
        self.require("quad.py")
