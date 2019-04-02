# Summation of primes
# Answer: 142913828922

from problem3 import is_prime


def sum_of_primes(limit):
    total = 0
    for i in range(2, limit):
        if is_prime(i):
            total += i
    return total


limit = 2000000
print(sum_of_primes(limit))
