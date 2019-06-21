# true dla listy > 10 i false < 10

def is_list_longer_than_ten(list_of_elements):
    if len(list_of_elements) > 10:
        return True
    else:
        return False


input_list = [1, 4, 7, 22, 50, 86, 95, 97, 99, 100, 101]
print(is_list_longer_than_ten(input_list))


# przypisac liczbe wystapien w stringu kazdej litery

def get_amount_of_letters(input_string):
    summarized_letters = {}
    for char in input_string:
        if summarized_letters.get(char) is None: # Nie ma jeszcze danego elementu w mapie
            summarized_letters[char] = 0

        summarized_letters[char] = summarized_letters[char] + 1

    return summarized_letters


def iterate_over(iterable):
    i = 0
    for element in iterable:
        print(i, element)

def iterate_over_with_value(iterable):
    i = 0
    for (key, element) in iterable.items():
        print("No: ", i, " with key: ", key, " has value: ", element)



iterate_over(["ty", "niedobry", "jarku"])
iterate_over("abcdefg")
iterate_over({1:"abc", 2:"gdte", 3:"potaek"})
iterate_over_with_value({1:"abc", 2:"gdte", 3:"potaek"})

string_pocz = "aaaa" + "bbb" + "cc" + "d"
print(get_amount_of_letters(string_pocz))