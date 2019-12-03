# Distinct powers
# Answer: 9183


def distinct_powers(start=2, end=100):
    powers = set()
    for a in range(start, end + 1):
        for b in range(start, end + 1):
            powers.add(a ** b)
    return len(powers)


start, end = map(int, input().split())
print(distinct_powers(start=start, end=end))
