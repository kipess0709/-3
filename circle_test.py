import unittest
import math
from circle import area, perimeter
class CircleTestCase(unittest.TestCase):

   #площадь
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_positive_area(self):
        res = area(10)
        self.assertAlmostEqual(res, math.pi * 100)
   
    def test_float_area(self):
        r = 4.2
        res = area(r)
        expected = math.pi * r * r
        self.assertAlmostEqual(res, expected, places=7)

    def test_large_area(self):
        r = 1e154
        res = area(r)
        expected = math.pi * r * r
        self.assertAlmostEqual(res, expected, places=7)

   #периметр
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_positive_perimeter(self):
        res = perimeter(10)
        self.assertAlmostEqual(res, 2 * math.pi * 10)
    
    def test_float_perimeter(self):
        r = 3.7
        res = perimeter(r)
        expected = 2 * math.pi * r
        self.assertAlmostEqual(res, expected, places=7)

    def test_large_perimeter(self):
        r = 1e154
        res = perimeter(r)
        expected = 2 * math.pi * r
        self.assertAlmostEqual(res, expected, places=7)

   
if __name__ == "__main__":
    unittest.main()