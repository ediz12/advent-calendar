# Day 5: Hydrothermal Venture - https://adventofcode.com/2021/day/5
with open("puzzle_inputs/day5.txt") as f:
    input_values = f.read()

input_values = input_values.split("\n")

max_x = 0
max_y = 0
for line in input_values:
    start, end = line.split(" -> ")
    (start_x, start_y) = [int(nr) for nr in start.split(",")]
    (end_x, end_y) = [int(nr) for nr in end.split(",")]
    if max_x < start_x:
        max_x = start_x
    if max_x < end_x:
        max_x = end_x
    if max_y < start_y:
        max_y = start_y
    if max_y < end_y:
        max_y = end_y


def points_to_mark(start_x: int, start_y: int, end_x: int, end_y: int, diagonal_enabled: bool = False) -> list:
    if start_y == end_y:
        if start_x > end_x:
            start_x, end_x = end_x, start_x
        return [(x, start_y) for x in range(start_x, end_x + 1)]
    elif start_x == end_x:
        if start_y > end_y:
            start_y, end_y = end_y, start_y
        return [(start_x, y) for y in range(start_y, end_y + 1)]
    elif diagonal_enabled:
        if start_x > end_x:
            x_range = reversed([x for x in range(end_x, start_x + 1)])
        else:
            x_range = [x for x in range(start_x, end_x + 1)]
        if start_y > end_y:
            y_range = reversed([y for y in range(end_y, start_y + 1)])
        else:
            y_range = [y for y in range(start_y, end_y + 1)]
        return [coord for coord in zip(x_range, y_range)]
    else:
        return list()


# SILVER ANSWER
board = [[0] * (max_x + 1) for _ in range(max_y + 1)]

for line in input_values:
    start, end = line.split(" -> ")
    (start_x, start_y) = [int(nr) for nr in start.split(",")]
    (end_x, end_y) = [int(nr) for nr in end.split(",")]
    for x, y in points_to_mark(start_x, start_y, end_x, end_y):
        board[y][x] += 1

total_overlapping_points = sum([1 for row in board for number in row if number > 1])
print(f"Silver answer: {total_overlapping_points}")

# GOLD ANSWER
board = [[0] * (max_x + 1) for _ in range(max_y + 1)]

for line in input_values:
    start, end = line.split(" -> ")
    (start_x, start_y) = [int(nr) for nr in start.split(",")]
    (end_x, end_y) = [int(nr) for nr in end.split(",")]
    for x, y in points_to_mark(start_x, start_y, end_x, end_y, diagonal_enabled=True):
        board[y][x] += 1

total_overlapping_points = sum([1 for row in board for number in row if number > 1])
print(f"Gold answer: {total_overlapping_points}")
