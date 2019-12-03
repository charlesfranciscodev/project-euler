# Multiples of 3 and 5
# Answer: 233168


def multiples_of_three_and_five(limit=1000):
    total = 0
    for i in range(1, limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

print(multiples_of_three_and_five())
