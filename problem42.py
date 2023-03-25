# Coded triangle numbers
# Answer: 162


def triangle_numbers(limit):
    numbers = {1}
    n = 2
    while max(numbers) < limit:
        number = n * (n + 1) / 2
        numbers.add(number)
        n += 1
    return numbers


def is_triangle_word(word, numbers):
    word_value = 0
    for c in word:
        word_value += ord(c) - ord('A') + 1
    return word_value in numbers


def solve(words, numbers):
    total = 0
    for word in words:
        if is_triangle_word(word, numbers):
            total += 1
    return total


if __name__ == "__main__":
    file_name = "p042_words.txt"
    with open(file_name, "r") as f:
        content = f.read()
        words = content.replace('\"', '').split(',')
        max_len = 0
        for word in words:
            max_len = max(max_len, len(word))
        limit = max_len * 26
        numbers = triangle_numbers(limit)
        print(solve(words, numbers))
