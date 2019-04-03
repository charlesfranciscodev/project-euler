# Power digit sum
# Answer: 1366


def power_digit_sum(exp):
    power = 2 ** exp
    return sum(map(int, list(str(power))))


exp = int(input())
print(power_digit_sum(exp))
