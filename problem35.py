# Circular primes
import unittest
from problem27 import is_prime


def is_circular_prime(x):
    s = str(x)
    for i in range(len(s)):
        rotation = s[i:] + s[:i]
        if not is_prime(int(rotation)):
            return False
    return True


def circular_primes():
    total = 0
    limit = 10 ** 6
    for x in range(2, limit):
        if is_circular_prime(x):
            total += 1
    return total


class TestCircularPrimes(unittest.TestCase):
    def test_1(self):
        expected = 55
        actual = circular_primes()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
