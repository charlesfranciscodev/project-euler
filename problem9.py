# Special Pythagorean triplet
# Answer: 31875000


def special_pythagorean_triplet(limit):
    c = 0
    m = 2
    while c < limit:
        for n in range(1, m):
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
            if c > limit:
                break
            if (a + b + c) == 1000:
                return (a, b, c)
        m = m + 1
    return None


a, b, c = special_pythagorean_triplet(1000)
product = a * b * c
print(a, b, c)
print(product)
