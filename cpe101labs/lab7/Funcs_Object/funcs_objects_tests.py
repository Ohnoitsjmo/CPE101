import unittest
from objects import *
import objects
from funcs_objects import *
import funcs_objects
import math

class TestCases(unittest.TestCase):
   def test_distance(self):
      my_point = objects.Point(1, 5)
      my_second_point = objects.Point(2,6)
      self.assertAlmostEqual(funcs_objects.distance(my_point, my_second_point), math.sqrt(2))

   def test_distance_2(self):
      my_point = objects.Point(5, 1)
      my_second_point = objects.Point(1, 5)
      self.assertAlmostEqual(funcs_objects.distance(my_point, my_second_point), math.sqrt(32))

   def test_point(self):
      my_point = objects.Point(1.2, 3.4)
      print("x-coord: ", my_point.x)
      print("y-coord: ", my_point.y)

   def test_point_2(self):
      my_point = objects.Point(5, 9)
      print("x-coord: ", my_point.x)
      print("y-coord: ", my_point.y)

   def test_circle(self):
      my_circle = objects.Circle((1, 1), 5)
      print("Center: ", my_circle.center)
      print("Radius: ", my_circle.radius)

   def test_circle_2(self):
      my_circle = objects.Circle((2, 1), 9)
      print("Center: ", my_circle.center)
      print("Radius: ", my_circle.radius)

   def test_overlap(self):
      my_circle_1 = objects.Circle((2, 1), 1)
      my_circle_2 = objects.Circle((3, 1), 1)
      self.assertEqual(funcs_objects.circles_overlap(my_circle_1, my_circle_2), True)

   def test_overlap_2(self):
      my_circle_1 = objects.Circle((2, 1), 1)
      my_circle_2 = objects.Circle((2, 9), 4)
      self.assertEqual(funcs_objects.circles_overlap(my_circle_1, my_circle_2), False)
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

