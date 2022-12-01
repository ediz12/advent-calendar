# Day 6: Probably a Fire Hazard - https://adventofcode.com/2015/day/6
with open("puzzle_inputs/day6.txt") as f:
    input_values = f.read()

input_values = input_values.split("\n")

# SILVER ANSWER
grid = [[0] * 1000 for _ in range(1000)]
for line in input_values:
    start_line, end_line = line.split(" through ")
    endX, endY = end_line.split(",")
    if start_line.startswith("turn off"):
        startX, startY = start_line.replace("turn off ", "").split(",")
        for y in range(int(startY), int(endY) + 1):
            for x in range(int(startX), int(endX) + 1):
                grid[y][x] = 0
    elif start_line.startswith("turn on"):
        startX, startY = start_line.replace("turn on ", "").split(",")
        for y in range(int(startY), int(endY) + 1):
            for x in range(int(startX), int(endX) + 1):
                grid[y][x] = 1
    elif start_line.startswith("toggle"):
        startX, startY = start_line.replace("toggle ", "").split(",")
        for y in range(int(startY), int(endY) + 1):
            for x in range(int(startX), int(endX) + 1):
                grid[y][x] = 1 if grid[y][x] == 0 else 0

print(f"Silver answer: {sum([1 for y in range(1000) for x in range(1000) if grid[y][x] == 1])}")

# GOLD ANSWER
grid = [[0] * 1000 for _ in range(1000)]
for line in input_values:
    start_line, end_line = line.split(" through ")
    endX, endY = end_line.split(",")
    if start_line.startswith("turn off"):
        startX, startY = start_line.replace("turn off ", "").split(",")
        for y in range(int(startY), int(endY) + 1):
            for x in range(int(startX), int(endX) + 1):
                grid[y][x] = max(0, grid[y][x] - 1)
    elif start_line.startswith("turn on"):
        startX, startY = start_line.replace("turn on ", "").split(",")
        for y in range(int(startY), int(endY) + 1):
            for x in range(int(startX), int(endX) + 1):
                grid[y][x] = grid[y][x] + 1
    elif start_line.startswith("toggle"):
        startX, startY = start_line.replace("toggle ", "").split(",")
        for y in range(int(startY), int(endY) + 1):
            for x in range(int(startX), int(endX) + 1):
                grid[y][x] = grid[y][x] + 2

print(f"Gold answer: {sum([grid[y][x] for y in range(1000) for x in range(1000)])}")
