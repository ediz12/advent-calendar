# Day 2: Rock Paper Scissors - https://adventofcode.com/2022/day/2
with open("puzzle_inputs/day2.txt") as f:
    input_values = f.read()

# SILVER ANSWER
# Rock: A, X
# Paper: B, Y
# Scissors: C, Z

# Answer here
turns = input_values.split("\n")

win_moves = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

draw_moves = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

lose_moves = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

move_scores = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

status_scores = {
    "win": 6,
    "draw": 3,
    "lose": 0
}

total_score = 0

for turn in turns:
    opponent_move, your_move = turn.split(" ")
    if your_move == draw_moves[opponent_move]:
        total_score += status_scores["draw"] + move_scores[your_move]
    elif your_move == win_moves[opponent_move]:
        total_score += status_scores["win"] + move_scores[your_move]
    else:
        total_score += status_scores["lose"] + move_scores[your_move]

print(f"Silver answer: {total_score}")

# GOLD ANSWER

total_score = 0

status_move = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}

for turn in turns:
    opponent_move, status_letter = turn.split(" ")
    status = status_move[status_letter]

    total_score += status_scores[status]
    if status == "win":
        total_score += move_scores[win_moves[opponent_move]]
    elif status == "draw":
        total_score += move_scores[draw_moves[opponent_move]]
    else:
        total_score += move_scores[lose_moves[opponent_move]]

# Answer here

print(f"Gold answer: {total_score}")
