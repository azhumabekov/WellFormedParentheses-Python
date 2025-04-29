import unittest
from count import countWellFormedParenthesis

class TestCountWellFormedParenthesis(unittest.TestCase):

    def test_small_values(self):
        self.assertEqual(countWellFormedParenthesis(0), 1)
        self.assertEqual(countWellFormedParenthesis(1), 1)
        self.assertEqual(countWellFormedParenthesis(2), 2)
        self.assertEqual(countWellFormedParenthesis(3), 5)
        self.assertEqual(countWellFormedParenthesis(4), 14)

    def test_negative(self):
        self.assertEqual(countWellFormedParenthesis(-1), 0)

    def test_large(self):
        self.assertEqual(countWellFormedParenthesis(10), 16796)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            countWellFormedParenthesis("3")
        with self.assertRaises(TypeError):
            countWellFormedParenthesis(None)
        with self.assertRaises(TypeError):
            countWellFormedParenthesis(3.5)
        with self.assertRaises(TypeError):
            countWellFormedParenthesis([3])

if __name__ == "__main__":
    unittest.main()