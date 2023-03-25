# 10001st prime
# Answer: 104743
from problem3 import is_prime


max_count = int(input())
i = 2
prime_number = i
count = 0
while count < max_count:
    if is_prime(i):
        prime_number = i
        count += 1
    i += 1
print(prime_number)
