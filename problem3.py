# Largest prime factor
# Answer: 6857
import math


def is_prime(i):
    end = math.floor(math.sqrt(i)) + 1
    for j in range(2, end):
        if i % j == 0:
            return False
    return True


def largest_prime_factor(x=600851475143):
    max_factor = 1
    i = 2
    end = math.floor(math.sqrt(x)) + 1
    while i < end:
        if x % i == 0:
            if is_prime(i):
                max_factor = max(max_factor, i)
        i += 1
    return max_factor


if __name__ == "__main__":
    x = int(input())
    print(largest_prime_factor(x))
