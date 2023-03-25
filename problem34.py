# Digit factorials
import math
import unittest


def is_curious_number(n):
    digits = str(n)
    total = 0
    for digit in digits:
        total += math.factorial(int(digit))
    return total == n


def sum_curious_numbers():
    total = 0
    for i in range(3, 10 ** 5):
        if is_curious_number(i):
            total += i
    return total


class TestSumCuriousNumbers(unittest.TestCase):
    def test_1(self):
        expected = 40730
        actual = sum_curious_numbers()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
