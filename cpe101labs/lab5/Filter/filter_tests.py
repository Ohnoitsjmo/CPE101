import unittest
import filter

class TestCases(unittest.TestCase):
   def test_1_are_positive(self):
      list_of_nums = [0, 1, 2]
      self.assertEqual(filter.are_positive(list_of_nums), [1, 2])
   
   def test_2_are_positive(self):
      list_of_nums = [-3, 4, 5]
      self.assertEqual(filter.are_positive(list_of_nums), [4, 5])
   
   def test_1_are_greater_than_n(self):
      list_of_nums = [1, 2, 3]
      n = 1
      self.assertEqual(filter.are_greater_than_n(list_of_nums, n), [2, 3])

   def test_2_are_greater_than_n(self):
      list_of_nums = [4, 5, 6]
      n = 5
      self.assertEqual(filter.are_greater_than_n(list_of_nums, n), [6])

   def test_1_are_divisible_by_n(self):
      list_of_nums = [2, 5, 8]
      n = 2
      self.assertEqual(filter.are_divisible_by_n(list_of_nums, n), [2, 8])

   def test_2_are_divisible_by_n(self):
      list_of_nums = [5, 6, 7]
      n = 3
      self.assertEqual(filter.are_divisible_by_n(list_of_nums, n), [6])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

