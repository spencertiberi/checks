from check50 import *

class Challenge(Checks):

	@check()
	def exists(self):
		"""calculator.py exists"""
		self.require("calculator.py")

    @check("exists")
    def test_add(self):
        """input of '2', '+', and '2' yields output of 4"""
        self.spawn("python calculator.py").stdin("378282246310005").stdout("^AMEX\n", "AMEX\n").exit(0)
