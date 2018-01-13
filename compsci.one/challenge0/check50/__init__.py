from check50 import *

class Challenge(Checks):

	@check()
	def exists(self):
		"""calculator.py exists"""
		self.require("calculator.py")

	@check("exist0")
    	def test_add(self):
		"""input of '2', '+', and '2' yields output of 4"""
		self.spawn("python calculator.py").stdin("2").stdin("+").stdin("2").stdout("4\n", "4\n").exit(0)
