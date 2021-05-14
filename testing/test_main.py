try:
    from AutoFeedback.plotchecks import check_plot
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.plotchecks import check_plot

from AutoFeedback.plotclass import line
from AutoFeedback.randomclass import randomvar
import unittest
from main import *

x = np.linspace(1,100,100)
var = randomvar( [prob,1-prob], variance=[prob*(1-prob),prob*(1-prob)], vmin=[0,0], vmax=[1,1], isinteger=[True,True] ) 
line1=line( x, var )

axislabels=["Outcome", "Probability"]

class UnitTests(unittest.TestCase) :
    def test_plot(self) :
        assert(check_plot([line1],explabels=axislabels,is_bar_chart=True,explegend=False,output=True))
