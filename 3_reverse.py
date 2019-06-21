# odwroc liste

def reverse_list(input_list):
    reversed_list = [None] * len(input_list)
    i = 0

    for elements in input_list:
        reversed_list[len(input_list) - 1 - i] = elements

        i = i+1

    return reversed_list


lista = [54, 5, 8, 51, 52]
print(reverse_list(lista))