import unittest
from main import modulo

class TestModuloFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(20, 4), 0)
        self.assertEqual(modulo(15, 4), 3)

    def test_negative_numbers(self):
        self.assertEqual(modulo(-10, 3), 2)
        self.assertEqual(modulo(10, -3), -2)

    def test_zero_division(self):
        self.assertRaises(ValueError, modulo, 10, 0)


if __name__ == "__main__":
    unittest.main()
