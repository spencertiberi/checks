from check50 import *

class Adlib(Checks):

    @check()
    def exists(self):
        """adlib.py exists."""
        self.require("adlibs.py")

    @check("exists")
    def test1(self):
        """Example Run works."""
        self.spawn("python adlibs.py").stdin("Tom Brady")\
		.stdin("stinky")\
		.stdin("blue")\
        .stdin("quietly")\
        .stdin("soup")\
        .stdin("bananas")\
        .stdin("button")\
        .stdin("Belmont")\
        .stdin("jump").stdout("Tom Brady was planning a dream vacation to Belmont.\nTom Brady was especially looking forward to trying the local\ncuisine, including stinky soup and bananas.\n\nTom Brady will have to practice the language quietly to\nmake it easier to jump with people.\n\nTom Brady has a long list of sights to see, including the\nbutton museum and the blue park.\n").exit(0)
