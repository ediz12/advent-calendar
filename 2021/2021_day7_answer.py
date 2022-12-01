# Day 7: The Treachery of Whales - https://adventofcode.com/2021/day/7
with open("puzzle_inputs/day7.txt") as f:
    input_values = f.read()

input_values = [int(i) for i in input_values.split(",")]
min_value = min(input_values)
max_value = max(input_values)

# SILVER ANSWER
absolute_distances = {}
for current_position in range(min_value, max_value):
    abs_list = []
    for input_position in input_values:
        abs_list.append(abs(current_position - input_position))
    absolute_distances[current_position] = sum(abs_list)

print(f"Silver answer: {min(absolute_distances.values())}")

# GOLD ANSWER
absolute_distances = {}
for current_position in range(min_value, max_value):
    abs_list = []
    for input_position in input_values:
        steps = abs(current_position - input_position)
        total_fuel = (steps * (steps + 1)) / 2
        abs_list.append(total_fuel)
    absolute_distances[current_position] = sum(abs_list)

print(f"Gold answer: {min(absolute_distances.values())}")
