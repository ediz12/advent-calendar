# Day 9: Smoke Basin - https://adventofcode.com/2021/day/9
with open("puzzle_inputs/day9.txt") as f:
    input_values = f.read()

input_values = input_values.split("\n")
'''input_values = """2199943210
3987894921
9856789892
8767896789
9899965678""".split()'''

height_map = [[int(nr) for nr in line] for line in input_values]
start_row = 0
end_row = len(height_map) - 1
start_column = 0
end_column = len(height_map[0]) - 1

# SILVER ANSWER
low_points = []

for row_index in range(end_row + 1):
    for column_index in range(end_column + 1):
        current_value = height_map[row_index][column_index]

        if row_index != start_row and height_map[row_index - 1][column_index] <= current_value:
            continue
        if row_index != end_row and height_map[row_index + 1][column_index] <= current_value:
            continue
        if column_index != start_column and height_map[row_index][column_index - 1] <= current_value:
            continue
        if column_index != end_column and height_map[row_index][column_index + 1] <= current_value:
            continue
        low_points.append(current_value)

risk_level = sum(low_points) + len(low_points)
print(f"Silver answer: {str(risk_level)}")

# GOLD ANSWER

# Answer here

print(f"Gold answer: {'answer'}")
