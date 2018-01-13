from check50 import *

class Challenge(Checks):

	@check()
	def exists(self):
		"""calculator.py exists"""
		self.require("calculator.py")

    @check("exists")
    def test(self):
        """input of 2 yeilds 2"""
        self.spawn("python calculator.py").stdin("2").stdout("2\n", "2\n").exit(0)
