import unittest
from rectangle import area, perimeter
class RectangleTestCase(unittest.TestCase):

   #площадь
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_positive_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
    
    def test_float_area(self):
        a = 4.6
        b = 2.3
        res = area(a, b)
        expected = a * b 
        self.assertAlmostEqual(res, expected, places=7)

    def test_large_area(self):
        a, b = 1e150, 2e150
        res = area(a, b)
        self.assertEqual(res, a*b)
   
   #периметр
    def test_zero_perimeter(self):
        res = perimeter(4,0)
        self.assertEqual(res, 8)

    def test_positive_perimeter(self):
        res = perimeter(2,4)
        self.assertEqual(res, 12)
    
    def test_float_perimeter(self):
        a = 4.6
        b = 2.3
        res = perimeter(a, b)
        expected = 2*(a + b)
        self.assertAlmostEqual(res, expected, places=7)

    def test_large_perimeter(self):
        a, b = 1e150, 2e150
        res = perimeter(a, b)
        self.assertEqual(res, 2*(a+b))

if __name__ == "__main__":
    unittest.main()