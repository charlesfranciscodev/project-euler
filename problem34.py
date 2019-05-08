# Digit factorials
# Answer: 40730

import math


def is_curious_number(n):
    digits = str(n)
    total = 0
    for digit in digits:
        total += math.factorial(int(digit))
    return total == n

      
if __name__ == "__main__":
    total = 0
    for i in range(3, 10 ** 5):
        if is_curious_number(i):
            total += i
    print(total)
