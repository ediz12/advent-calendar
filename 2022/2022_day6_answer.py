# Day 6: Tuning Trouble - https://adventofcode.com/2022/day/6
with open("puzzle_inputs/day6.txt") as f:
    input_values = f.read()

# SILVER ANSWER

# Answer here

answer = 0
for i in range(0, len(input_values)):
    current_pattern_list = list(input_values[i:i + 4])
    current_pattern_set = set(input_values[i:i + 4])
    if len(current_pattern_list) == len(current_pattern_set):
        answer = i + 4
        break

print(f"Silver answer: {answer}")

# GOLD ANSWER

# Answer here

for i in range(0, len(input_values)):
    current_pattern_list = list(input_values[i:i + 14])
    current_pattern_set = set(input_values[i:i + 14])
    if len(current_pattern_list) == len(current_pattern_set):
        answer = i + 14
        break

print(f"Gold answer: {answer}")
