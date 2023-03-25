# Even Fibonacci numbers
# Answer: 4613732


def even_fibonnaci_numbers(limit=4000000):
    total = 2
    sequence = [1, 2]
    i = 1
    while True:
        current = sequence[i - 1] + sequence[i]
        if current >= limit:
            break
        sequence.append(current)
        if current % 2 == 0:
            total += current
        i += 1
    return total


print(even_fibonnaci_numbers())
