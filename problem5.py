# Smallest multiple
# Answer: 232792560


def is_divisible(x, min_value, max_value):
    for y in range(min_value, max_value + 1):
        if x % y != 0:
            return False
    return True


def smallest_multiple(min_value, max_value):
    x = max_value + 1
    while True:
        if is_divisible(x, min_value, max_value):
            return x
        x += 1


if __name__ == "__main__":
    print("Please enter the min and max values separated by a space: ", end='')
    min_value, max_value = map(int, input().split())
    print(smallest_multiple(min_value, max_value))
