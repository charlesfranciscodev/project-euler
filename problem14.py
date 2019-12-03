# Longest Collatz sequence
# Answer: 837799


def len_collatz_sequence(x):
    count = 1
    while x != 1:
        if x % 2 == 0:
            x /= 2
        else:
            x = 3 * x + 1
        count += 1
    return count


def solve(max_start_value=10**6):
    max_count = 1
    value_for_longest_chain = 1
    for i in range(3, max_start_value):
        count = len_collatz_sequence(i)
        if count > max_count:
            max_count = count
            value_for_longest_chain = i
    return value_for_longest_chain


print(solve())
