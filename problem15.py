# Lattice paths
# Answer: 137846528820

import math


def binomial_coefficient(x):
    n = x * 2
    k = x
    return int(math.factorial(n) / (math.factorial(n - k) * math.factorial(k)))


x = int(input())
print(binomial_coefficient(x))
