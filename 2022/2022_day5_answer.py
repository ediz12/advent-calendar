# Day 5: Supply Stacks - https://adventofcode.com/2022/day/5
import re

with open("puzzle_inputs/day5.txt") as f:
    input_values = f.read()

# SILVER ANSWER
# Answer here
crates_input, command_input = input_values.split("\n\n")
crates_input_list = crates_input.split("\n")

names_list = " ".join(crates_input_list[-1].split())
crates_list = crates_input_list[:-1]


def initialize_stacks_map():
    stacks_map = {name: [] for name in names_list.split()}

    for crates_index in range(len(crates_list), 0, -1):

        current_crates_str = crates_list[crates_index - 1]

        for enumerated_index, char_index in enumerate(range(1, len(current_crates_str), 4)):

            current_char = current_crates_str[char_index]
            current_stack_name = str(enumerated_index + 1)

            if current_char != " ":
                stacks_map[current_stack_name].append(current_char)

    return stacks_map


stacks_map = initialize_stacks_map()

for command in command_input.split("\n"):
    amount_to_move, from_stack, to_stack = re.findall("\d+", command)

    crates_to_move = reversed(stacks_map[from_stack][-int(amount_to_move):])
    stacks_map[from_stack] = stacks_map[from_stack][:-int(amount_to_move)]
    stacks_map[to_stack].extend(crates_to_move)

answer = ""
for stacks in stacks_map.values():
    answer += stacks[-1]

print(f"Silver answer: {answer}")

# GOLD ANSWER
# Answer here

stacks_map = initialize_stacks_map()

for command in command_input.split("\n"):
    amount_to_move, from_stack, to_stack = re.findall("\d+", command)

    crates_to_move = stacks_map[from_stack][-int(amount_to_move):]
    stacks_map[from_stack] = stacks_map[from_stack][:-int(amount_to_move)]
    stacks_map[to_stack].extend(crates_to_move)

answer = ""
for stacks in stacks_map.values():
    answer += stacks[-1]
print(f"Gold answer: {answer}")
