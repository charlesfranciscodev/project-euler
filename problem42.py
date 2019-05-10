# Double-base palindromes
# Answer: 162


def triangle_numbers(limit):
    numbers = [1]
    index = 2
    while numbers[-1] < limit:
        next_number = index * (index + 1) / 2
        numbers.append(next_number)
        index += 1
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
        numbers = set(triangle_numbers(limit))
        print(solve(words, numbers))
