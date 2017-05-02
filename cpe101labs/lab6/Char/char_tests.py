import unittest
import char

class TestChar(unittest.TestCase):
   def test_lower_1(self):
      self.assertEqual(char.is_lower_101('A'), False)

   def test_lower_2(self):
      self.assertEqual(char.is_lower_101('a'), True)

   def test_rot_13_1(self):
      self.assertEqual(char.char_rot_13('B'), 'O')
   
   def test_rot_13_2(self):
      self.assertEqual(char.char_rot_13('b'), 'o')
if __name__ == '__main__':
   unittest.main()

