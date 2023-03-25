# Number letter counts
# Answer: 21124

import inflect

p = inflect.engine()
limit = int(input())
total = 0
for i in range(1, limit + 1):
    total += len(p.number_to_words(i).replace(' ', '').replace('-', ''))
print(total)
