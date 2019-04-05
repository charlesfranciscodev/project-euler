# Amicable numbers
# Answer: 31626

import math


def proper_divisors(n):
    divisors = {1}
    limit = int(math.sqrt(n))
    for i in range(2, limit):
        if n % i == 0:
            n2 = n // i
            divisors.add(i)
            if n2 != n:
                divisors.add(n2)
    return divisors


amicable_numbers = set()
for x in range(1, 10000):
    divisors_x = proper_divisors(x)
    y = sum(divisors_x)
    divisors_y = proper_divisors(y)
    if x == sum(divisors_y) and x != y:
        amicable_numbers.add(x)
        amicable_numbers.add(y)
print(sum(amicable_numbers))
