# Day 4: The Ideal Stocking Stuffer - https://adventofcode.com/2015/day/4
with open("puzzle_inputs/day4.txt") as f:
    input_values = f.read()

import hashlib

# SILVER ANSWER
lowest_number = 0
while True:
    hash = hashlib.md5(f"{input_values}{str(lowest_number)}".encode("utf-8")).hexdigest()
    if str(hash).startswith("00000"):
        break
    lowest_number += 1

print(f"Silver answer: {lowest_number}")

# GOLD ANSWER
lowest_number = 0
while True:
    hash = hashlib.md5(f"{input_values}{str(lowest_number)}".encode("utf-8")).hexdigest()
    if str(hash).startswith("000000"):
        break
    lowest_number += 1

print(f"Gold answer: {lowest_number}")
