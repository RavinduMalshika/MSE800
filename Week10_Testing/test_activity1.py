import unittest
import activity1

class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = activity1.add(2, 3)
        self.assertEqual(result, 5)

    def test_divide(self):
        result = activity1.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            activity1.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
