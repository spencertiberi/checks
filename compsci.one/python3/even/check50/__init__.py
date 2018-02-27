from check50 import *

class Even(Checks):

    @check()
    def exists(self):
        """even.py exists."""
        self.require("even.py")

    @check("exists")
    def test1(self):
        """Prints 1 odd, 2 even, ..."""
        self.spawn("python even.py").stdout("1 odd\n2 even\n3 odd\n4 even\n5 odd\n6 even\n7 odd\n8 even\n9 odd\n10 even\n11 odd\n12 even\n13 odd\n14 even\n15 odd\n").exit(0)
