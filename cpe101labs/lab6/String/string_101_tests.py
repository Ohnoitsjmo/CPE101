import unittest
from string_101 import *

import unittest
import string_101

class TestString(unittest.TestCase):
   def test_1_rot(self):
      self.assertEqual(str_rot_13('hello'), 'uryyb')

   def test_2_rot(self):
      self.assertEqual(str_rot_13('HELLO'), 'URYYB')

   def test_1_translate(self):
      self.assertEqual(str_translate_101('Hello', 'l', 'y'), 'Heyyo')

   def test_2_translate(self):
      self.assertEqual(str_translate_101('Happy', 'p', 'k'), 'Hakky')
if __name__ == '__main__':
   unittest.main()

