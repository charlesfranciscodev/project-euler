# Distinct powers
# Answer: 9183


def distinct_powers(start_a, end_a, start_b, end_b):
    powers = set()
    for a in range(start_a, end_a + 1):
        for b in range(start_b, end_b + 1):
            powers.add(a ** b)
    return powers


start_a, end_a, start_b, end_b = map(int, input().split())
print(len(distinct_powers(start_a, end_a, start_b, end_b)))
