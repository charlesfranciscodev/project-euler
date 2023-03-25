# Double-base palindromes
import unittest


def is_a_double_base_palindrome(x):
    x_in_base2 = bin(x)[2:]
    x_in_base10 = str(x)
    return x_in_base2 == x_in_base2[::-1] and x_in_base10 == x_in_base10[::-1]


def sum_double_base_palindromes():
    total = 0
    limit = 10 ** 6
    for x in range(1, limit):
        if is_a_double_base_palindrome(x):
            total += x
    return total


class TestSumDoubleBasePalindromes(unittest.TestCase):
    def test_1(self):
        expected = 872187
        actual = sum_double_base_palindromes()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
