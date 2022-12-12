import unittest
from gen import lazy_gen
import time

class gen_test(unittest.TestCase):
  def test_1(self):
    a=[i for i in (lazy_gen(5))]
    b=[0,1,1,2,3]
    self.assertEqual(a,b)

  def test_2(self):
    start = time.time()
    a=[i for i in lazy_gen(99999)]
    end = time.time()-start
    self.assertLess(end,1)
  def test_3(self):
    start = time.time()
    a=(i for i in lazy_gen(99999))
    end = time.time()-start
    startt = time.time()
    a=[i for i in lazy_gen(99999)]
    endd = time.time()-startt
    self.assertLess(endd,end)
if __name__=='__main__':
  unittest.main()