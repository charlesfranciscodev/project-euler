# Factorial digit sum
# Answer: 648

import math


def factorial_digit_sum(n=10**3):
    return sum(map(int, list(str(math.factorial(n)))))


n = int(input())
print(factorial_digit_sum(n=n))
