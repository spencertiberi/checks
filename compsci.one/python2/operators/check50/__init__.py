from check50 import *

class Adlib(Checks):

    @check()
    def exists(self):
        """adlibs.py exists."""
        self.require("adlibs.py")

    @check("exists")
    def test1(self):
        """Example run works."""
        self.spawn("python adlibs.py").stdin("Tom Brady")\
		.stdin("stinky")\
		.stdin("blue")\
        .stdin("quietly")\
        .stdin("soup")\
        .stdin("bananas")\
        .stdin("button")\
        .stdin("Belmont")\
        .stdin("jump").stdout("Tom Brady was planning a dream vacation to Belmont.\nTom Brady was especially looking forward to trying the local\ncuisine, including stinky soup and bananas.\n\nTom Brady will have to practice the language quietly to\nmake it easier to jump with people.\n\nTom Brady has a long list of sights to see, including the\nbutton museum and the blue park.\n").exit(0)

    @check("exists")
    def test2(self):
        """Tests novel input."""
        self.spawn("python adlibs.py").stdin("LeBron")\
		.stdin("yellow")\
		.stdin("French")\
        .stdin("stupidly")\
        .stdin("toast")\
        .stdin("rice")\
        .stdin("fart")\
        .stdin("Boise")\
        .stdin("lose").stdout("LeBron was planning a dream vacation to Boise.\nLeBron was especially looking forward to trying the local\ncuisine, including yellow toast and rice.\n\nLeBron will have to practice the language stupidly to\nmake it easier to lose with people.\n\nLeBron has a long list of sights to see, including the\nfart museum and the French park.\n").exit(0)
