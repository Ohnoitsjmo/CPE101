import unittest
import fold

class TestCases(unittest.TestCase):
   def test_1_sum(self):
      list_of_nums = [1, 2, 3]
      self.assertEqual(fold.sum(list_of_nums), 6)   
 
   def test_2_sum(self):
      list_of_nums = [5, 6, 9, 12]
      self.assertEqual(fold.sum(list_of_nums), 32)

   def test_1_index_of_smallest(self):
      list_of_nums = [3, 2, 1, 2, 3]
      self.assertEqual(fold.index_of_smallest(list_of_nums), 2)
   
   def test_2_index_of_smallest(self):
      list_of_nums = []
      self.assertEqual(fold.index_of_smallest(list_of_nums), -1)

   def test_3_index_of_smallest(self):
      list_of_nums = [1, 2, 3, 2, 1]
      self.assertEqual(fold.index_of_smallest(list_of_nums), 0)
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

