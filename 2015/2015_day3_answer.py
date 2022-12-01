# Day 3: Perfectly Spherical Houses in a Vacuum - https://adventofcode.com/2015/day/3
with open("puzzle_inputs/day3.txt") as f:
    input_values = f.read()


def move_map(gift_map: dict, character: str, current_x: int, current_y: int):
    if character == "^":
        current_y += 1
    elif character == ">":
        current_x += 1
    elif character == "v":
        current_y -= 1
    elif character == "<":
        current_x -= 1
    try:
        gift_map[(current_x, current_y)] += 1
    except KeyError:
        gift_map[(current_x, current_y)] = 1
    return current_x, current_y


# SILVER ANSWER
gift_map = {(0, 0): 1}
current_xy = (0, 0)
for character in input_values:
    current_xy = move_map(gift_map, character, current_xy[0], current_xy[1])

print(f"Silver answer: {len(gift_map.keys())}")

# GOLD ANSWER
gift_map = {(0, 0): 1}
current_santa_xy = (0, 0)
current_robo_xy = (0, 0)
santa_turn = True
for character in input_values:
    if santa_turn:
        current_santa_xy = move_map(gift_map, character, current_santa_xy[0], current_santa_xy[1])
    else:
        current_robo_xy = move_map(gift_map, character, current_robo_xy[0], current_robo_xy[1])
    santa_turn = not santa_turn

print(f"Gold answer: {len(gift_map.keys())}")
