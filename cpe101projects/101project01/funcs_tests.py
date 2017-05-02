 # Project 1
 #
 # Name: Justin Mo
 # Instructor: Brian Jones
 # Section: 17

import unittest
import funcs
import math

class TestCases(unittest.TestCase):

   def test_pounds_to_kg(self):
      self.assertEqual(funcs.pounds_to_kg(5), 2.26796)
   def test_pounds_to_kg2(self):
      self.assertEqual(funcs.pounds_to_kg(6), 2.721552)

   def test_get_mass_object(self):
      self.assertEqual(funcs.get_mass_object("r"), 3.0)
   def test_get_mass_object_2(self):
      self.assertEqual(funcs.get_mass_object("g"), 5.3)

   def test_get_velocity_object(self):
      self.assertAlmostEqual(funcs.get_velocity_object(1), 2.2135943621)
   def test_get_velocity_object_2(self):
      self.assertAlmostEqual(funcs.get_velocity_object(2), 3.1304951684)

   def test_get_velocity_skater(self):
      self.assertEqual(funcs.get_velocity_skater(1,2,3), 6)
   def test_get_velocity_skater2(self):
      self.assertEqual(funcs.get_velocity_skater(5,6,7), 8.4)

if __name__ == '__main__':
   unittest.main()
