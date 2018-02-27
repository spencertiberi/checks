from check50 import *

class Lister(Checks):

    @check()
    def exists(self):
        """lister.py exists."""
        self.require("lister.py")

    @check("exists")
    def test1(self):
        """Input of 3, "pizza", "cheese", "pineapple" works"""
        self.spawn("python lister.py").stdin('3').stdin('pizza').stdin('cheese').stdin('pineapple').stdout("['pizza', 'cheese', 'pineapple']\n").exit(0)

    @check("exists")
    def test2(self):
        """Input of 4, "pizza", "cheese", "pineapple", "anchovies" works"""
        self.spawn("python lister.py").stdin('4')\
		.stdin('pizza')\
        .stdin('cheese')\
        .stdin('pineapple')\
        .stdin('anchovies').stdout("[\'pizza\', \'cheese\', \'pineapple\', \'anchovies\']\n").exit(0)
