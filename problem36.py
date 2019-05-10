# Double-base palindromes
# Answer: 872187


def is_a_double_base_palindrome(x):
    x_in_base2 = bin(x)[2:]
    x_in_base10 = str(x)
    return x_in_base2 == x_in_base2[::-1] and x_in_base10 == x_in_base10[::-1]

     
if __name__ == "__main__":
    total = 0
    limit = 10 ** 6
    for x in range(1, limit):
        if is_a_double_base_palindrome(x):
            print(x, bin(x))
            total += x
    print(total)
