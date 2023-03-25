# Largest palindrome product
import unittest


def is_palindrome(number):
    s = str(number)
    return s == s[::-1]


def largest_palindrome_product(nb_digits=3):
    min_value = 10 ** (nb_digits - 1)
    max_value = 10 ** nb_digits
    max_product = 0
    for i in range(min_value, max_value):
        for j in range(min_value, max_value):
            product = i * j
            if is_palindrome(product) and product > max_product:
                max_product = product
    return max_product


class TestLargestPalindromeProduct(unittest.TestCase):
    def test_1(self):
        expected = 906609
        actual = largest_palindrome_product()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
