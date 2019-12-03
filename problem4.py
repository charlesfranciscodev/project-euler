# Largest palindrome product
# Answer: 906609


def is_palindrome(number):
    s = str(number)
    return s == s[::-1]


def largest_palindrome(nb_digits=3):
    min_value = 10 ** (nb_digits - 1)
    max_value = 10 ** nb_digits
    max_product = 0
    for i in range(min_value, max_value):
        for j in range(min_value, max_value):
            product =  i * j
            if is_palindrome(product) and product > max_product:
                max_product = product
    return max_product


if __name__ == "__main__":
    print("Enter the number of digits: ")
    nb_digits = int(input())
    print(largest_palindrome(nb_digits=nb_digits))
