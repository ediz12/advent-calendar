# Day 2: Cube Conundrum - https://adventofcode.com/2023/day/2
with open("puzzle_inputs/day2.txt") as f:
    input_values = f.read()

played_games = input_values.split("\n")
max_color_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

# SILVER ANSWER
total = 0

for played_game in played_games:
    game_id_text, picked_cube_set = played_game.split(": ")
    picked_cube_set = picked_cube_set.split("; ")

    game_id = int(game_id_text.replace("Game ", ""))
    is_possible_game = True

    for picked_cubes in picked_cube_set:
        color_cubes = picked_cubes.split(", ")
        for color_cube in color_cubes:
            picked_number, color = color_cube.split()
            if int(picked_number) > max_color_cubes[color]:
                is_possible_game = False

    if is_possible_game:
        total += game_id


print(f"Silver answer: {total}")

# GOLD ANSWER
total = 0

for played_game in played_games:
    game_id_text, picked_cube_set = played_game.split(": ")
    picked_cube_set = picked_cube_set.split("; ")

    game_id = int(game_id_text.replace("Game ", ""))
    max_color_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for picked_cubes in picked_cube_set:
        color_cubes = picked_cubes.split(", ")
        for color_cube in color_cubes:
            picked_number, color = color_cube.split()
            if int(picked_number) > max_color_cubes[color]:
                max_color_cubes[color] = int(picked_number)

    total += max_color_cubes["red"] * max_color_cubes["green"] * max_color_cubes["blue"]


print(f"Gold answer: {total}")
