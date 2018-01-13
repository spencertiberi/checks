from check50 import *


class Credit(Checks):

    @check()
    def exists(self):
        """credit.py exists."""
        self.require("credit.py")

    @check("exists")
    def test1(self):
        """input of 2 yields 2"""
        self.spawn("python credit.py").stdin("2").stdout("2\n", "2\n").exit(0)

    @check("exists")
    def test2(self):
        """identifies 371449635398431 as AMEX"""
        self.spawn("python credit.py").stdin("371449635398431").stdout("^AMEX\n", "AMEX\n").exit(0)

    @check("exists")
    def test3(self):
        """identifies 5555555555554444 as MASTERCARD"""
        self.spawn("python credit.py").stdin("5555555555554444").stdout("^MASTERCARD\n", "MASTERCARD\n").exit(0)

    @check("exists")
    def test4(self):
        """identifies 5105105105105100 as MASTERCARD"""
        self.spawn("python credit.py").stdin("5105105105105100").stdout("^MASTERCARD\n", "MASTERCARD\n").exit(0)

    @check("exists")
    def test5(self):
        """identifies 4111111111111111 as VISA"""
        self.spawn("python credit.py").stdin("4111111111111111").stdout("^VISA\n", "VISA\n").exit(0)

    @check("exists")
    def test6(self):
        """identifies 4012888888881881 as VISA"""
        self.spawn("python credit.py").stdin("4012888888881881").stdout("^VISA\n", "VISA\n").exit(0)

    @check("exists")
    def test7(self):
        """identifies 1234567890 as INVALID"""
        self.spawn("python credit.py").stdin("1234567890").stdout("^INVALID\n", "INVALID\n").exit(0)

    @check("exists")
    def test_reject_foo(self):
        """rejects a non-numeric input of "foo" """
        self.spawn("python credit.py").stdin("foo").reject()

    @check("exists")
    def test_reject_empty(self):
        """rejects a non-numeric input of "" """
        self.spawn("python credit.py").stdin("").reject()
