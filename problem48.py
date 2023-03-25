# Self powers
# Answer: 9110846700


def self_powers(limit=1001):
    total = 0
    for x in range(1, limit):
        total += x ** x
    return str(total)[-10:]


if __name__ == "__main__":
    print(self_powers())
