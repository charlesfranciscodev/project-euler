# Highly divisible triangular number
# Answer: 76576500

import math


def divisors_count(number):
    count = 0
    limit = math.ceil(math.sqrt(number))
    for i in range(1, limit):
        if number % i == 0:
            if number / i == i:
                count += 1
            else:
                count += 2
    return count


def solve(count):
    i = 1
    triangular_number = i
    while True:
        if divisors_count(triangular_number) >= count:
            return triangular_number
        i += 1
        triangular_number += i


if __name__ == "__main__":
    count = int(input())
    print(solve(count))
