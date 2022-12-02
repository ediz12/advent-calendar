# Day 10: Syntax Scoring - https://adventofcode.com/2021/day/10
with open("puzzle_inputs/day10.txt") as f:
    input_values = f.read()

# SILVER ANSWER

# Answer here
lines = input_values.split("\n")
chunks_map = {
    "<": ">",
    "(": ")",
    "[": "]",
    "{": "}"
}
chunks_map_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

total_score = 0
for chunks_line in lines:
    chunks = list(chunks_line)
    last_chunks = ""
    for chunk in chunks:
        if chunk in chunks_map:
            last_chunks = last_chunks + chunk
        else:
            if chunks_map[last_chunks[-1]] == chunk:
                last_chunks = last_chunks[:-1]
            else:
                total_score += chunks_map_points[chunk]
                break

print(f"Silver answer: {total_score}")

# GOLD ANSWER

# Answer here

print(f"Gold answer: {'answer'}")
