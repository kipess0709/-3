import unittest
from square import area, perimeter
class SquareTestCase(unittest.TestCase):

    #площадь
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_square_area(self):
        res = area(10)
        self.assertEqual(res, 100)
   
    def test_float_area(self):
        a = 3.8
        expected = a * a 
        self.assertAlmostEqual(area(a), expected, places=7)

    def test_large_area(self):
        a = 1e150
        res = area(a)
        self.assertEqual(res, a**2)

    #периметр
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_square_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 20)
    
    def test_float_perimeter(self):
        a = 3.8
        expected = 4 * a 
        self.assertAlmostEqual(perimeter(a), expected, places=7)

    def test_large_perimeter(self):
        a = 1e150
        res = perimeter(a)
        self.assertEqual(res, 4*a)


if __name__ == "__main__":
    unittest.main()