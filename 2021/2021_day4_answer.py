# Day 4: Giant Squid - https://adventofcode.com/2021/day/4
with open("puzzle_inputs/day4.txt") as f:
    input_values = f.read()

input_values = input_values.split("\n")
draw_numbers = input_values[0].split(",")
columns = [column.split() for board in "\n".join(input_values[2:]).split("\n\n") for column in board.split("\n")]
boards = [columns[i:i + 5] for i in range(0, len(columns), 5)]


def check_is_bingo(board):
    row_bingo = any([all([number.startswith("*") for number in row]) for row in board])
    column_bingo = any([all([row[i].startswith("*") for row in board]) for i in range(5)])
    return row_bingo or column_bingo


# SILVER ANSWER
bingo_board = []
last_drawn_number = 0
is_bingo = False
for current_nr in draw_numbers:
    if not is_bingo:
        for board in boards:
            for row in board:
                for index, number in enumerate(row):
                    if current_nr == number:
                        row[index] = f"*{number}"
            if check_is_bingo(board):
                is_bingo = True
                bingo_board = board
                last_drawn_number = int(current_nr)

sum_of_unmarked_numbers = sum([int(number) for row in bingo_board for number in row if not number.startswith("*")])

print(f"Silver answer: {sum_of_unmarked_numbers * last_drawn_number}")

# GOLD ANSWER
last_bingo_board = []
last_drawn_number = 0
is_last_board = False
for current_nr in draw_numbers:
    if not is_last_board:
        boards_to_remove = []
        for board in boards:
            for row in board:
                for index, number in enumerate(row):
                    if current_nr == number:
                        row[index] = f"*{number}"
            if check_is_bingo(board):
                if len(boards) == 1:
                    last_bingo_board = board
                    last_drawn_number = int(current_nr)
                    is_last_board = True
                else:
                    boards_to_remove.append(board)
        for board in boards_to_remove:
            boards.remove(board)

sum_of_unmarked_numbers = sum([int(number) for row in last_bingo_board for number in row if not number.startswith("*")])

print(f"Gold answer: {sum_of_unmarked_numbers * last_drawn_number}")
