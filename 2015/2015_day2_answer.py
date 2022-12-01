# Day 2: I Was Told There Would Be No Math - https://adventofcode.com/2015/day/2
with open("puzzle_inputs/day2.txt") as f:
    input_values = f.read()

input_values = input_values.split("\n")
# SILVER ANSWER
total_papers = sum([(2 * (int(l) * int(w) + int(w) * int(h) + int(h) * int(l))) + min(
    [int(l) * int(w), int(w) * int(h), int(h) * int(l)]) for line in input_values for l, w, h in [line.split("x")]])
print(f"Silver answer: {total_papers}")

# GOLD ANSWER
total_ribbon = sum([(2 * int(l) + 2 * int(w) + 2 * int(h) - 2 * max(int(l), int(w), int(h)))
                + (int(l) * int(w) * int(h)) for line in input_values for l, w, h in [line.split("x")]])
print(f"Gold answer: {total_ribbon}")
