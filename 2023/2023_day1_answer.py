# Day 1: Trebuchet?! - https://adventofcode.com/2023/day/1
with open("puzzle_inputs/day1.txt") as f:
    input_values = f.read()

import re

# SILVER ANSWER
total = 0

for calibration_data in input_values.split("\n"):
    matches = re.findall("\d", calibration_data)
    total += int(matches[0] + matches[-1])

print(f"Silver answer: {total}")

# GOLD ANSWER
number_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

total = 0

for calibration_data in input_values.split("\n"):
    matches = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', calibration_data)
    matches_string = "".join(matches)
    for word, number in number_map.items():
        matches_string = matches_string.replace(word, number)

    total += int(matches_string[0] + matches_string[-1])

print(f"Gold answer: {total}")
