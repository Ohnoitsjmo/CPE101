import unittest
import conditional

class TestCases(unittest.TestCase):
   def test_max_101(self):
      self.assertEqual(conditional.max_101(1,2),2)
      
   def test_max_101_2(self):
      self.assertEqual(conditional.max_101(2,3),3)

   def test_max_of_three(self):
      self.assertEqual(conditional.max_of_three(1,2,3),3.0)

   def test_max_of_three_2(self):
      self.assertEqual(conditional.max_of_three(2,3,4),4.0)

   def test_rental_late_fee(self):
      self.assertEqual(conditional.rental_late_fee(25),100)

   def test_rental_late_fee_2(self):
      self.assertEqual(conditional.rental_late_fee(9),5)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

