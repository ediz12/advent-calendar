# Day 4: Camp Cleanup - https://adventofcode.com/2022/day/4
with open("puzzle_inputs/day4.txt") as f:
    input_values = f.read()

# SILVER ANSWER
total_all_overlap = 0
total_any_overlap = 0
for line in input_values.split("\n"):
    first_sections_range, second_sections_range = line.split(",")
    first_start_section, first_end_section = first_sections_range.split("-")
    second_start_section, second_end_section = second_sections_range.split("-")

    first_sections = list(range(int(first_start_section), int(first_end_section) + 1))
    second_sections = list(range(int(second_start_section), int(second_end_section) + 1))
    if all([number in second_sections for number in first_sections]) or \
            all([number in first_sections for number in second_sections]):
        total_all_overlap += 1
    if any([number in second_sections for number in first_sections]) or \
            any([number in first_sections for number in second_sections]):
        total_any_overlap += 1


# Answer here

print(f"Silver answer: {total_all_overlap}")

# GOLD ANSWER
for line in input_values.split("\n"):
    first_sections_range, second_sections_range = line.split(",")
    first_start_section, first_end_section = first_sections_range.split("-")
    second_start_section, second_end_section = second_sections_range.split("-")

    first_sections = list(range(int(first_start_section), int(first_end_section) + 1))
    second_sections = list(range(int(second_start_section), int(second_end_section) + 1))
# Answer here

print(f"Gold answer: {total_any_overlap}")
