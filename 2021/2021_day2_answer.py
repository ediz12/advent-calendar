# Day 2: Dive! - https://adventofcode.com/2021/day/2
with open("puzzle_inputs/day2.txt") as f:
    input_values = f.read()

input_values = input_values.split("\n")

# SILVER ANSWER
horizontal = 0
depth = 0

for request in input_values:
    path, move_value = request.split()
    move_value = int(move_value)
    if path == "up":
        depth -= move_value
    elif path == "down":
        depth += move_value
    elif path == "forward":
        horizontal += move_value

print(f"Silver answer: {horizontal * depth}")

# GOLD ANSWER
horizontal = 0
depth = 0
aim = 0

for request in input_values:
    path, move_value = request.split()
    move_value = int(move_value)
    if path == "up":
        aim -= move_value
    elif path == "down":
        aim += move_value
    elif path == "forward":
        horizontal += move_value
        depth += aim * move_value

print(f"Gold answer: {horizontal * depth}")
