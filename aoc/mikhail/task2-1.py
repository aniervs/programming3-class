def sum_calibration_values(lines):
    total_sum = 0
    for line in lines:
        digits = [char for char in line if char.isdigit()]
        if digits:
            number = int(digits[0] + digits[-1])
            total_sum += number
    return total_sum

file_path = 'aoc/mikhail/puzzles_input/puzzle1.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

result = sum_calibration_values(lines)
print(result)
