import unittest
import logic

class TestCases(unittest.TestCase):
   def test_is_even(self):
      self.assertTrue(logic.is_even(2))

   def test_is_even_2(self):
      self.assertFalse(logic.is_even(5))
 
   def test_in_an_interval(self):
      self.assertEqual(logic.in_an_interval(17),True)

   def test_in_an_interval2(self):
      self.assertEqual(logic.in_an_interval(104),False)
     

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

