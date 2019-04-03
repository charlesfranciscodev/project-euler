# Names scores
# Answer: 871198282

with open("p022_names.txt") as f:
    s = f.read()

names = sorted(s.replace('\"', '').split(','))

total_score = 0
for i, name in enumerate(names):
    alphabetical_value = 0
    for c in name:
        alphabetical_value += ord(c) - ord('A') + 1
    score = alphabetical_value * (i + 1)
    total_score += score

print(total_score)
