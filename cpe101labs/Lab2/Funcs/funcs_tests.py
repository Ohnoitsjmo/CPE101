import unittest
import funcs
import math

class TestCases(unittest.TestCase):
   def test_f(self):
      self.assertEqual(funcs.f(4),120)

   def test_f2(self):
      self.assertEqual(funcs.f(5),185) 

   def test_g(self):
      self.assertAlmostEqual(funcs.g(2,3),2.166666666666)
    
   def test_g2(self):
      self.assertAlmostEqual(funcs.g(3,2),1.44444444444)  
    
   def test_hypotenuse(self):
      self.assertEqual(funcs.hypotenuse(4,3),5.0)

   def test_hypotenuse2(self):
      self.assertAlmostEqual(funcs.hypotenuse(4,5),6.4031242374328)

   def test_is_positive(self):
      self.assertEqual(funcs.is_positive(2),True)

   def test_is_positive2(self):
      self.assertEqual(funcs.is_positive(-1),False)
 # Add code here.
   
  


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

