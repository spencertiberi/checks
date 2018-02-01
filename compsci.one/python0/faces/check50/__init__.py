import re

from check50 import *

class Faces(Checks):

    @check()
    def exists(self):
        """faces.py exists."""
        self.require("faces.py")

    @check("exists")
    def prints_faces(self):
        """prints "faces correctly\\n" """
        expected = "^ ^\n _\n\nQ('.'Q)\n\n? ?\n >\n~~~\n"
        actual = self.spawn("python faces.py").stdout()
        if not re.match(expected, actual):
            err = Error(Mismatch("^ ^\n _\n\nQ('.'Q)\n\n? ?\n >\n~~~\n", actual))
            if re.match(expected[:-1], actual):
                err.helpers = "Perhaps your whitespace doesn't match exactly?"
            raise err
