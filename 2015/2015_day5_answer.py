# Day 5: Doesn't He Have Intern-Elves For This? - https://adventofcode.com/2015/day/5
with open("puzzle_inputs/day5.txt") as f:
    input_values = f.read()

input_values = input_values.split()

# SILVER ANSWER
vowels = list("aeiou")
banned_strings = ["ab", "cd", "pq", "xy"]
nice_count = 0
for string in input_values:
    if any([banned_string in string for banned_string in banned_strings]):
        continue

    if sum([1 for letter in string if letter in vowels]) < 3:
        continue

    if any([string[i] == string[i + 1] for i in range(len(string) - 1)]):
        nice_count += 1

print(f"Silver answer: {str(nice_count)}")


# GOLD ANSWER
nice_count = 0
for string in input_values:
    combinations = [string[i] + string[i + 1] for i in range(len(string) - 1)]
    dupe_combinations = set(combinations)
    if len(combinations) == len(dupe_combinations):
        continue

    if not any([combinations[i] in string[i + 2:] for i in range(len(combinations))]):
        continue

    rule_2_pass = any([combinations[i][0] == combinations[i + 1][1]  for i in range(len(combinations) - 1)])
    if not rule_2_pass:
        continue

    nice_count += 1

print(f"Gold answer: {str(nice_count)}")
