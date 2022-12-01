# Day 1: Calorie Counting - https://adventofcode.com/2022/day/1
with open("puzzle_inputs/day1.txt") as f:
    input_values = f.read()

# SILVER ANSWER
calories_str_by_elf = [str_calories for str_calories in input_values.split("\n\n")]
calories_by_elf = []
for calories_str in calories_str_by_elf:
    calories = [int(calorie) for calorie in calories_str.split("\n")]
    calories_by_elf.append(calories)

sums_of_calories_by_elf = sorted([sum(calories) for calories in calories_by_elf], reverse=True)
answer = max(sums_of_calories_by_elf)
# Answer here

print(f"Silver answer: {answer}")

# GOLD ANSWER

# Answer here
answer =  sum(sums_of_calories_by_elf[0:3])

print(f"Gold answer: {answer}")
