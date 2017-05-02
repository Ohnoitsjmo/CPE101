import unittest
import map

class TestCases(unittest.TestCase):
   def test_1_square_all(self):
      list_of_nums = [1, 2, 3, 4]
      self.assertEqual(map.square_all(list_of_nums), [1, 4, 9, 16])      
 
   def test_2_square_all(self):
      list_of_nums = [4, 3, 2, 1]
      self.assertEqual(map.square_all(list_of_nums), [16, 9, 4, 1])
   
   def test_1_add_n_all(self):
      list_of_nums = [1, 2, 3]
      n = 1
      self.assertEqual(map.add_n_all(list_of_nums,n), [2, 3, 4])

   def test_2_add_n_all(self):
      list_of_nums = [4, 5, 6]
      n = 2
      self.assertEqual(map.add_n_all(list_of_nums,n), [6, 7, 8])

   def test_1_even_or_odd_all(self):
      list_of_nums = [1, 2, 3]
      self.assertEqual(map.even_or_odd_all(list_of_nums), [False, True, False])

   def test_2_even_or_odd_all(self):
      list_of_nums = [4, 5, 6]
      self.assertEqual(map.even_or_odd_all(list_of_nums), [True, False, True])
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

