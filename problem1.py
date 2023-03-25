# Multiples of 3 and 5
import unittest


def multiples_of_three_and_five(limit=1000):
    total = 0
    for i in range(1, limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


class TestMultiplesOfThreeAndFive(unittest.TestCase):
    def test_1(self):
        expected = 233168
        actual = multiples_of_three_and_five()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
