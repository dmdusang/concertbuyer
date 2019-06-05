import unittest
from fractions import Fraction
import my_sum
from my_sum import sum
class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result,6)

    def test_list_fration(self):
        """
        Test that i can sum a list of fractions
        """
        data = [Fraction(1,4), Fraction(1,4), Fraction(2,5)]
        result = sum(data)
        self.assertEqual(result,1)

if __name__ == '__main__':
    unittest.main()
