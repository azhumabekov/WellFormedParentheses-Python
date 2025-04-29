import unittest
from main import countWellFormedParenthesis

class TestCountParenthesis(unittest.TestCase):

    def test_small_values(self):
        self.assertEqual(countWellFormedParenthesis(0), 1)
        self.assertEqual(countWellFormedParenthesis(1), 1)
        self.assertEqual(countWellFormedParenthesis(2), 2)
        self.assertEqual(countWellFormedParenthesis(3), 5)
        self.assertEqual(countWellFormedParenthesis(4), 14)

    def test_negative(self):
        self.assertEqual(countWellFormedParenthesis(-1), 0)

if __name__ == '__main__':
    unittest.main()