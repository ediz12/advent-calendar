# Day 6: Lanternfish - https://adventofcode.com/2021/day/6
with open("puzzle_inputs/day6.txt") as f:
    input_values = f.read()

input_values = [int(i) for i in input_values.split(",")]

from collections import Counter

# SILVER ANSWER
lantern_fishes = Counter(input_values)
for day in range(80):
    new_fishes = lantern_fishes[0]
    for timer in [1, 2, 3, 4, 5, 6]:
        lantern_fishes[timer - 1] = lantern_fishes[timer]
    lantern_fishes[6] = lantern_fishes[7] + new_fishes
    lantern_fishes[7] = lantern_fishes[8]
    lantern_fishes[8] = new_fishes

print(f"Silver answer: {sum(lantern_fishes.values())}")

# GOLD ANSWER
lantern_fishes = Counter(input_values)
for day in range(256):
    new_fishes = lantern_fishes[0]
    for timer in [1, 2, 3, 4, 5, 6]:
        lantern_fishes[timer - 1] = lantern_fishes[timer]
    lantern_fishes[6] = lantern_fishes[7] + new_fishes
    lantern_fishes[7] = lantern_fishes[8]
    lantern_fishes[8] = new_fishes

print(f"Gold answer: {sum(lantern_fishes.values())}")
