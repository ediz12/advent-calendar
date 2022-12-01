# Day 1: Not Quite Lisp - https://adventofcode.com/2015/day/1
with open("puzzle_inputs/day1.txt") as f:
    input_values = f.read()

# SILVER ANSWER
floor = sum([1 if character == "(" else -1 for character in input_values])
print(f"Silver answer: {floor}")

# GOLD ANSWER
floor = 0
first_basement_position = 0

for position, character in enumerate(list(input_values)):
    if character == "(":
        floor += 1
    else:
        floor -= 1
    if floor < 0:
        first_basement_position = position + 1
        break

print(f"Gold answer: {first_basement_position}")
