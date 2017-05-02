import unittest
import poly

class TestPoly(unittest.TestCase):

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_poly_add(self):
      poly1 = [2.3, 4.7, 1.0]
      poly2 = [1.2, 2.1, -3.2]
      poly3 = poly.poly_add2(poly1, poly2)
      self.assertListAlmostEqual(poly3, [3.5, 6.8, -2.2])

   def test_poly_add_2(self):
      poly1 = [4, 6, 8]
      poly2 = [2, 3, 4]
      poly3 = poly.poly_add2(poly1, poly2)
      self.assertListAlmostEqual(poly3, [6, 9, 12])

   def test_poly_mult(self):
      poly1 = [3, 2, 1]
      poly2 = [6, 5, 4]
      poly3 = poly.poly_mult2(poly1, poly2)
      self.assertListAlmostEqual(poly3, [18, 27, 28, 13, 4])
   
   def test_poly_mult_2(self):
      poly1 = [2, 3, 4]
      poly2 = [1, 2, 3]
      poly3 = poly.poly_mult2(poly1, poly2)
      self.assertListAlmostEqual(poly3, [2, 7, 16, 17, 12])

if __name__ == '__main__':
   unittest.main()
