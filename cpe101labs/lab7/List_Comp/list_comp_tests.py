import unittest
from list_comp import *
import list_comp
from objects import *
import objects
import math

class TestCases(unittest.TestCase):
   def test_distance_all(self):
      my_point = objects.Point(1, 2)
      my_point_1 = objects.Point(2, 3)
      my_point_2 = objects.Point(4, 5) 
      list_of_points = [my_point, my_point_1, my_point_2]
      self.assertAlmostEqual(list_comp.distance_all(list_of_points), [math.sqrt(5), math.sqrt(13), math.sqrt(41)])

   def test_distance_all_1(self):
      my_point = objects.Point(5, 4)
      my_point_1 = objects.Point(2, 1)
      my_point_2 = objects.Point( 3, 2)
      list_of_points = [my_point, my_point_1, my_point_2]
      self.assertAlmostEqual(list_comp.distance_all(list_of_points), [math.sqrt(41), math.sqrt(5), math.sqrt(13)])
   
   def test_are_in_first_quadrant(self):
      my_point = objects.Point(1, 2)
      my_point_1 = objects.Point(2, 3)
      my_point_2 = objects.Point(4, 5)
      list_of_points = [my_point, my_point_1, my_point_2]
      self.assertEqual(list_comp.are_in_first_quadrant(list_of_points), [(1, 2), (2, 3), (4, 5)])

   def test_are_in_first_quadrant_1(self):
      my_point = objects.Point(-1, 2)     
      my_point_1 = objects.Point(-2, 3)
      my_point_2 = objects.Point(4, 5)
      list_of_points = [my_point, my_point_1, my_point_2]
      self.assertEqual(list_comp.are_in_first_quadrant(list_of_points), [(4, 5)])
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
