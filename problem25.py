# 1000-digit Fibonacci number
# Answer: 4782


def last_term_contains(sequence, nb_digits):
    last_term = sequence[-1]
    return len(str(last_term)) == nb_digits


def solve(nb_digits):
    sequence = [1, 1]
    while not last_term_contains(sequence, nb_digits):
        n = len(sequence)
        term = sequence[n - 2] + sequence[n - 1]
        sequence.append(term)
    return len(sequence)


nb_digits = int(input())
print(solve(nb_digits))
