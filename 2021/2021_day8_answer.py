# Day 8: Seven Segment Search - https://adventofcode.com/2021/day/8
with open("puzzle_inputs/day8.txt") as f:
    input_values = f.read()

input_values = input_values.split("\n")

# SILVER ANSWER
basic_segment_count = 0
for line in input_values:
    _, segment_output = line.split(" | ")
    basic_segment_count += sum([1 for segment in segment_output.split() if len(segment) in [2, 4, 3, 7]])

print(f"Silver answer: {str(basic_segment_count)}")

# GOLD ANSWER
#  dddd  TOP
# e    a TOP LEFT, TOP RIGHT
# e    a TOP LEFT, TOP RIGHT
#  ffff  MIDDLE
# g    b BOTTOM LEFT, BOTTOM RIGHT
# g    b BOTTOM LEFT, BOTTOM RIGHT
#  cccc  BOTTOM

# 0 --> 6 letters, ALL OF THEM except MIDDLE
# 1 --> 2 letters, TOP RIGHT, BOTTOM RIGHT
# 2 --> 5 letters, TOP, TOP RIGHT, MIDDLE, BOTTOM LEFT, BOTTOM
# 3 --> 5 letters, TOP, TOP RIGHT, MIDDLE, BOTTOM RIGHT, BOTTOM
# 4 --> 4 letters  TOP RIGHT, BOTTOM RIGHT, MIDDLE, TOP LEFT
# 5 --> 5 letters, TOP, TOP LEFT, MIDDLE, BOTTOM RIGHT, BOTTOM
# 6 --> 6 letters, TOP, TOP LEFT, MIDDLE, BOTTOM LEFT, BOTTOM RIGHT, BOTTOM
# 7 --> 3 letters  TOP RIGHT, BOTTOM RIGHT, TOP
# 8 --> 7 letters  ALL OF THEM
# 9 --> 6 letters, ALL OF THEM except BOTTOM LEFT

total_of_output_numbers = 0

for line in input_values:
    signal_patterns, output_values = line.split(" | ")
    signal_letters_map = {}
    for signal in signal_patterns.split():
        if len(signal) == 2:
            signal_letters_map[1] = list(signal)
        elif len(signal) == 3:
            signal_letters_map[7] = list(signal)
        elif len(signal) == 4:
            signal_letters_map[4] = list(signal)
        elif len(signal) == 7:
            signal_letters_map[8] = list(signal)

    for signal in signal_patterns.split():
        if len(signal) == 6: # 0, 6, 9
            if all([char in signal for char in signal_letters_map[4]]):
                signal_letters_map[9] = list(signal)
            elif all([char in signal for char in signal_letters_map[1]]):
                signal_letters_map[0] = list(signal)
            else:
                signal_letters_map[6] = list(signal)

    for signal in signal_patterns.split():
        if len(signal) == 5: # 2, 3, 5
            if all([char in signal for char in signal_letters_map[1]]):
                signal_letters_map[3] = list(signal)
            elif all([char in signal_letters_map[9] for char in signal]):
                signal_letters_map[5] = list(signal)
            else:
                signal_letters_map[2] = list(signal)

    output_number = ""
    for output_value in output_values.split():
        for digit, segment in signal_letters_map.items():
            if len(segment) == len(output_value) and all([value in segment for value in output_value]):
                output_number += str(digit)

    total_of_output_numbers += int(output_number)

print(f"Gold answer: {str(total_of_output_numbers)}")
