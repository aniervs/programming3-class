spell_mapping = {'one': 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

with open('task1.txt', 'r') as file:
    content = file.read()

lines = content.split('\n')
total_sum = 0


def get_digit_or_spell_reverse(row, col):
    if lines[row][col].isdigit():
        return int(lines[row][col])

    for length in [5, 4, 3, 2]:
        if col - length + 1 >= 0 and lines[row][col - length + 1: col + 1] in spell_mapping:
            return spell_mapping[lines[row][col - length + 1: col + 1]]

    return 0


def get_digit_or_spell(row, col):
    if lines[row][col].isdigit():
        return int(lines[row][col])

    for length in [4, 3, 5]:
        if col + length - 1 < len(lines[row]) and lines[row][col: col + length] in spell_mapping:
            return spell_mapping[lines[row][col: col + length]]

    return 0


for row in range(len(lines)):
    start_index = 0
    end_index = len(lines[row]) - 1
    str_sum = ''

    while start_index < len(lines[row]):
        if get_digit_or_spell(row, start_index):
            str_sum += str(get_digit_or_spell(row, start_index))
            break
        start_index += 1

    while end_index >= 0:
        if get_digit_or_spell_reverse(row, end_index):
            str_sum += str(get_digit_or_spell_reverse(row, end_index))
            break
        end_index -= 1

    total_sum += int(str_sum)

print(total_sum)
