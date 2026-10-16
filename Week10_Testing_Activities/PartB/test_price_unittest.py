import unittest
import main

class TestCase(unittest.TestCase):
    def test_single_item_price(self):
        result = main.calculate_price(10, 1)
        self.assertEqual(result , 10)
        
    def test_several_items_price(self):
        result = main.calculate_price(20, 5)
        self.assertEqual(result, 100)
        
    def test_discount(self):
        result = main.calculate_price(10, 1, 10)
        self.assertAlmostEqual(result, 9)
        
    def test_two_decimal_points(self):
        result = main.calculate_price(10, 1, 10)
        self.assertEqual(result, 9)
        
if __name__ == '__main__':
    unittest.main()
