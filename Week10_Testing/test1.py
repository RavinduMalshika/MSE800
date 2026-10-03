import unittest #	imports the framework.

class TestCalculator(unittest.TestCase): # inherits from unittest.TestCase

    def test_add(self): # A test method starts with test_
        result = 10 + 5
        self.assertEqual(result, 15) # compares the actual and expected values

if __name__ == "__main__":
    unittest.main() # starts the test runner when the file is executed
