# Self powers
# Answer: 9110846700


if __name__ == "__main__":
    total = 0
    for x in range(1, 1001):
        total += x ** x
    print(total)
