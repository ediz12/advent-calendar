# Day 1: Sonar Sweep - https://adventofcode.com/2021/day/1
with open("puzzle_inputs/day1.txt") as f:
    input_values = f.read()

input_values = [int(i) for i in input_values.split("\n")]

# SILVER ANSWER
increased = 0

for i in range(len(input_values)):
    if i == len(input_values) - 1:
        break
    if input_values[i] < input_values[i + 1]:
        increased += 1

print(f"Silver answer: {increased}")

# GOLD ANSWER
increased = 0

for i in range(len(input_values)):
    try:
        if input_values[i] + input_values[i + 1] + input_values[i + 2] < input_values[i + 1] + input_values[i + 2] + input_values[i + 3]:
            increased += 1
    except IndexError:
        continue

print(f"Gold answer: {increased}")
