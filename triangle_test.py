import unittest
from triangle import area, perimeter
class TriangleTestCase(unittest.TestCase):

   #площадь
    def test_zero_area(self):
       res = area(2,0)
       self.assertEqual(res, 0)

    def test_triangle_area(self):
       res = area(2,3)
       self.assertEqual(res, 3)
   
    def test_float_area(self):
        a = 3.8
        h = 2.1
        res = area(a,h)
        expected = (a * h) / 2
        self.assertAlmostEqual(res, expected, places=7)
    
    def test_large_area(self):
        a, h = 1e150, 2e150
        res = area(a, h)
        self.assertEqual(res, a*h / 2)

    #периметр
    def test_zero_perimeter(self):
      res = perimeter(4,0,2)
      self.assertEqual(res, 6)

    def test_triangle_perimeter(self):
      res = perimeter(3,4,5)
      self.assertEqual(res, 12)
    
    def test_float_perimeter(self):
       a = 3.8
       b = 4.1
       c = 5.6
       res = perimeter(a,b,c)
       expected = a + b + c
       self.assertAlmostEqual(res, expected, places=7)
    
    def test_large_perimeter(self):
        a, b, c = 1e150, 2e150, 1e150
        res = perimeter(a, b, c)
        self.assertEqual(res, a+b+c)

if __name__ == "__main__":
    unittest.main()