# Even Fibonacci numbers
# Answer: 4613732

total = 2
sequence = [1,2]

i = len(sequence) - 1
while True:
    current = sequence[i - 1] + sequence[i]
    if current >= 4000000:
        break
    sequence.append(current)
    if current % 2 == 0:
        total += current
    i += 1
print(total)
