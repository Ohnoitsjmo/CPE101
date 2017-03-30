import unittest
import convert
class TestChar(unittest.TestCase):
   def test_convert_1(self):
      self.assertEqual(convert.float_default("xyz", 73), 73)   
   def test_convert_2(self):
      self.assertEqual(convert.float_default("5.35", 42), 5.35)
   def test_convert_3(self):
      self.assertEqual(convert.float_default("6.23", 55), 6.23)
   def test_convert_4(self):
      self.assertEqual(convert.float_default("lol", 32), 32)
if __name__ == '__main__':
   unittest.main()

