import unittest
from lab1re import get_roots
class TestLab1(unittest.TestCase):
  def test_noroot(self):
    coef = get_roots(1,11,10)
    self.assertEqual(len(coef),0)
    
  def test_oneroot(self):
    coef = get_roots(10,0,0)
    self.assertEqual(len(coef),1)
    self.assertEqual(coef, [0])
  def test_tworoot(self):
    coef = get_roots(1,-2,-8)
    self.assertEqual(len(coef),2)
    self.assertEqual(coef, [-2,2])
  #def test_threeroot(self):
    #coef = get_roots(-4,16,0)
    #self.assertEqual(len(coef),3)
    #self.assertEqual(coef, [-2,0,2])
  def test_fourroot(self):
    coef = get_roots(1,-10,9)
    self.assertEqual(len(coef),4) 
    self.assertEqual(coef, [-3,-1,1,3]) 
if __name__ == '__main__':
    unittest.main()