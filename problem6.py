# Sum square difference
# Answer: 25164150

def sum_of_the_squares(min_value, max_value):
    total = 0
    for i in range(min_value, max_value + 1):
        total += i ** 2
    return total


def square_of_the_sum(min_value, max_value):
    total = 0
    for i in range(min_value, max_value + 1):
        total += i
    return total ** 2


def sum_square_difference(min_value, max_value):
    return square_of_the_sum(min_value, max_value) - sum_of_the_squares(min_value, max_value)


if __name__ == "__main__":
    print("Please enter the min and max values separated by a space: ", end='')
    min_value, max_value = map(int, input().split())
    print(sum_square_difference(min_value, max_value))
