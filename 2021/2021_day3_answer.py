# Day 3: Binary Diagnostic - https://adventofcode.com/2021/day/3
with open("puzzle_inputs/day3.txt") as f:
    input_values = f.read()

input_values = input_values.split()
character_count = len(input_values[0])

# SILVER ANSWER
gamma_rate = ""
epsilon_rate = ""
for i in range(character_count):
    binary_digits = [int(binary_number[i]) for binary_number in input_values]
    gamma_rate += str(max(binary_digits, key=binary_digits.count))
    epsilon_rate += str(min(binary_digits, key=binary_digits.count))

print(f"Silver answer: {int(gamma_rate, 2) * int(epsilon_rate, 2)}")

# GOLD ANSWER
from copy import deepcopy
from collections import Counter

most_commons_list = deepcopy(input_values)
least_commons_list = deepcopy(input_values)


def get_max_digit_value(digits: list) -> str:
    ctr = Counter(digits)
    if len(ctr.most_common()) == 1:
        return str(ctr.most_common()[0][0])
    elif ctr.get(0) == ctr.get(1):
        return "1"
    return str(ctr.most_common()[0][0])


def get_min_digit_value(digits: list) -> str:
    ctr = Counter(digits)
    if len(ctr.most_common()) == 1:
        return str(ctr.most_common()[0][0])
    elif ctr.get(0) == ctr.get(1):
        return "0"
    return str(ctr.most_common()[1][0])


for i in range(character_count):
    if len(most_commons_list) > 0:
        binary_digits = [int(binary_number[i]) for binary_number in most_commons_list]
        max_digit_count_value = get_max_digit_value(binary_digits)
        temp_most_common_list = deepcopy(most_commons_list)
        for binary_number in temp_most_common_list:
            if binary_number[i] != max_digit_count_value:
                most_commons_list.remove(binary_number)

    if len(least_commons_list) > 0:
        binary_digits = [int(binary_number[i]) for binary_number in least_commons_list]
        min_digit_count_value = get_min_digit_value(binary_digits)
        temp_least_common_list = deepcopy(least_commons_list)
        for binary_number in temp_least_common_list:
            if binary_number[i] != min_digit_count_value:
                least_commons_list.remove(binary_number)

oxygen_generator_rating = most_commons_list[0]
co2_scrubber_rating = least_commons_list[0]

print(f"Gold answer: {int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)}")
