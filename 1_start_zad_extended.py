# zgadywanie

import random

class GameStatistics:
    def __init__(self, user_min, user_max, provided_num, rand_num):
        self.user_min = user_min
        self.user_max = user_max
        self.provided_num = provided_num
        self.rand_num = rand_num

        print("Statistics for range", user_min, user_max)
        print("The provided numbers are: ", provided_num)

        # diff to juz kazdy element listy w kolejnych iteracjach
        for diff in provided_num:
            print("The difference between", diff, "and", rand_num, "is", abs(rand_num - diff))

    def print_game_state(self):
        print("Your game state is:", self.user_min, self.user_max, self.provided_num, self.rand_num)


def get_input_and_increment(provided_num, min_by_user, max_by_user):
    # user_input = int(input())
    user_input = random.randint(min_by_user, max_by_user)
    provided_num.append(user_input)
    return user_input


def play_game():
    print("------------------------------------")
    print("Provide range (a,b)")
    user_min = random.randint(1, 50)
    print("From a:\t", user_min)

    user_max = random.randint(51, 100)
    print("To b:\t", user_max)

    rand_num = random.randint(user_min, user_max)

    print("Guess number in your range")

    provided_num = []
    user_input = get_input_and_increment(provided_num, user_min, user_max)

    while True:
        print("The generated number is: ", rand_num)
        print("Your number is: ", user_input)

        if user_input < user_min or user_input > user_max:
            print("You are out of range!")
            user_input = get_input_and_increment(provided_num, user_min, user_max)

        if user_input > rand_num:
            print("The number has to be lower")
            user_input = get_input_and_increment(provided_num, user_min, rand_num)
        elif user_input < rand_num:
            print("The number has to be bigger")
            user_input = get_input_and_increment(provided_num, rand_num, user_max)
        elif user_input == rand_num:
            print("This is the right number!")
            break

    print("Victory!")

    print("\nYou provided ", len(provided_num), " numbers.")

    if len(provided_num) == 1:
        print("\nYou cheated, mothafucka!")

    return GameStatistics(user_min, user_max, provided_num, rand_num)


print("------------------------------------")

no_of_games = random.randint(1, 5)

print("How many games do you want to play?\t", no_of_games)

game_stats = []

for how_many in range(no_of_games):
    game_stats.append(play_game())

for game_stat in game_stats:
    game_stat.print_game_state()

# napisac funkcje grającą w tę grę. Input ma miec min, max, obecna liczbe i  to czy jest wieksza lub mniejsza. Dodatkowy argument - 0 lub null.
# Kod, który w jak najmniejszej liczbie ruchów będzie grał sam ze sobą. Inicjalizacja na samym początku. Full automat dla inputa.

# (max - min) / 2
# osobna funkcja, która dostaje przedział i czy licza ma byc mniejsza czy wieksza