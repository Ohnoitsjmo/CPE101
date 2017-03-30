import unittest
from objects import *
import objects
import utility
from utility import *

class TestCases(unittest.TestCase):
   def test_equality(self):
      my_point_1 = objects.Point(1.2, 3.4)      
      my_point_2 = objects.Point(1.2, 3.4)
      self.assertTrue(my_point_1 == my_point_2)    

   def test_equality_2(self):
      my_point_1 = objects.Point(1.2, 3.6)
      my_point_2 = objects.Point(1.2, 3.5)
      self.assertFalse(my_point_1 == my_point_2)  
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

