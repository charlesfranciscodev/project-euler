# Quadratic primes
# Answer: -59231

import math


def is_prime(i):
    if i < 0:
        return False
    end = int((math.sqrt(i)) + 1)
    for j in range(2, end):
        if i % j == 0:
            return False
    return True


def nb_consecutive_primes(a, b):
    n = 0
    while True:
        number = n ** 2 + a * n + b
        if not is_prime(number):
            return n
        n += 1

           
if __name__ == "__main__":
    max_n = 0
    best_a = 0
    best_b = 0
    for a in range(-999, 1000):
        for b in range(-999, 1000):
              n = nb_consecutive_primes(a, b)
              if n > max_n:
                  max_n = n
                  best_a = a
                  best_b = b
    print(best_a * best_b)
