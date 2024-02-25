with open('task1.txt', 'r') as file:
    content = file.read()

lines = content.split('\n')
total_sum = 0

def get_digit_at_position(row, col, reverse=False):
    index = col if not reverse else len(lines[row]) - 1 - col
    if lines[row][index].isdigit():
        return int(lines[row][index])
    return 0

for row in range(len(lines)):
    start_index = 0
    end_index = len(lines[row]) - 1
    str_sum = ''

    while start_index < len(lines[row]):
        if get_digit_at_position(row, start_index):
            str_sum += str(get_digit_at_position(row, start_index))
            break
        start_index += 1

    while end_index >= 0:
        if get_digit_at_position(row, end_index, reverse=True):
            str_sum += str(get_digit_at_position(row, end_index, reverse=True))
            break
        end_index -= 1

    total_sum += int(str_sum)

print(total_sum)
