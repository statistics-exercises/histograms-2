import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_plot( self ) :
        n, bar = 0, np.sqrt( prob*(1-prob) )*st.norm.ppf( (0.99 + 1) / 2 )
        fighand = plt.gca()
        for p in fighand.patches :
           x, y = p.get_xy() 
           self.assertTrue( (x+0.5*p.get_width()-n)<1e-7, "the x-coordiantes in your graph are incorrect" )
           if n==0 : self.assertTrue( np.fabs( p.get_height() - 1 + prob )<bar, "the height of the bars in your graph appear to be incorrect" )
           else : self.assertTrue( np.fabs( p.get_height() - prob )<bar, "the height of the bars in your graph appear to be incorrect" )
           n=n+1.
