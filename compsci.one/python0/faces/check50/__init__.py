from check50 import *

class Faces(Checks):

    @check()
    def exists(self):
        """faces.py exists."""
        self.require("faces.py")

    @check("exists")
    def test1(self):
        """prints faces correctly."""
        self.spawn("python faces.py").stdout("^ ^\n -\n\nQ('.'Q)\n\n? ?\n >\n~~~\n", "^ ^\n -\n\nQ('.'Q)\n\n? ?\n >\n~~~\n").exit(0)
