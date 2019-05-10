# Circular primes
# Answer: 55

from problem27 import is_prime


def is_circular_prime(x):
    s = str(x)
    for i in range(len(s)):
        rotation = s[i:] + s[:i]
        if not is_prime(int(rotation)):
            return False
    return True
      
     
if __name__ == "__main__":
    total = 0
    limit = 10 ** 6
    for x in range(2, limit):
        if is_circular_prime(x):
            total += 1
    print(total)
