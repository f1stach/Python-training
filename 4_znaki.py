# f. pobiera pierwsze dwa i ostatnie dwa i je skleja

# ab ddd ce -> abec
# abc -> abcb
# ab -> abba
# a -> aa
# "" -> ""


def reverse_list(input_list):
    reversed_list = [" "] * len(input_list)
    i = 0

    for elements in input_list:
        reversed_list[:(len(input_list) - 1 - i)] = elements
        i = i+1
    return reversed_list


def get_letters_from_word(input_word):

    reversed_end = reverse_list(input_word[-2:])

    return input_word[:2] + ''.join(reversed_end)

init_list = []
words = ["ab ddd ce", "abc", "ab", "a"]
for word in words:
    print("Slowo to ", word, "a po sklejeniu", get_letters_from_word(word))
    # print(reverse_list(word))


# listy i petle!