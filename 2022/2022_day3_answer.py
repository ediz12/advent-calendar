# Day 3: Rucksack Reorganization - https://adventofcode.com/2022/day/3
with open("puzzle_inputs/day3.txt") as f:
    input_values = f.read()

# SILVER ANSWER

# Answer here
all_common_chars = list()
for line in input_values.split("\n"):
    first_half_chars = line[:len(line) // 2]
    second_half_chars = line[len(line) // 2:]
    common_chars = set(first_half_chars).intersection(set(second_half_chars))
    all_common_chars.extend(common_chars)

total_points = sum([ord(char) - 96 if char.islower() else ord(char) - 38 for char in all_common_chars])
print(f"Silver answer: {total_points}")

# GOLD ANSWER
# Answer here
all_common_chars = list()
input_values_list = input_values.split("\n")
input_values_grouped = [input_values_list[i:i + 3] for i in range(0, len(input_values_list), 3)]

for grouped_input in input_values_grouped:
    common_chars = set(grouped_input[0]).intersection(grouped_input[1], grouped_input[2])
    all_common_chars.extend(common_chars)

total_points = sum([ord(char) - 96 if char.islower() else ord(char) - 38 for char in all_common_chars])
print(f"Gold answer: {total_points}")
