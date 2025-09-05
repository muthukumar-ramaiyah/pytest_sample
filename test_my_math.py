# test_my_math.py
import unittest
from my_math import add

class TestMath(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

    def test_add_large_numbers(self):
        self.assertEqual(add(1000000, 2000000), 3000000)

    def test_add_float(self):
        self.assertAlmostEqual(add(2.5, 3.1), 5.6)

    def test_add_negative_and_positive(self):
        self.assertEqual(add(-5, 10), 5)

    def test_add_both_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_add_with_none(self):
        with self.assertRaises(TypeError):
            add(None, 1)

    def test_add_string(self):
        with self.assertRaises(TypeError):
            add("a", 1)

if __name__ == "__main__":
    unittest.main()

