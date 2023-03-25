# Non-abundant sums
import math
import unittest


def proper_divisors(n):
    divisors = {1}
    i = 2
    end = math.floor(math.sqrt(n)) + 1
    while i < end:
        if n % i == 0:
            divisors.add(i)
            divisors.add(n / i)
        i += 1
    return divisors


def abundant_numbers():
    numbers = set()
    for i in range(2, 28123):
        if sum(proper_divisors(i)) > i:
            numbers.add(i)
    return numbers


def non_abundant_sums():
    total = 0
    number_set = abundant_numbers()
    number_list = sorted(list(number_set))
    for i in range(1, 28123):
        cannot_be_written_as_the_sum = True
        for n in number_list:
            j = 0
            if i < n:
                break
            else:
                j = i - n
                if j in number_set:
                    cannot_be_written_as_the_sum = False
                    break

        if cannot_be_written_as_the_sum:
            total += i
    return total


class TestNonAbundantSums(unittest.TestCase):
    def test_1(self):
        expected = 4179871
        actual = non_abundant_sums()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
