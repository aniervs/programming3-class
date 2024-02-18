
def find_calibration_value_from_line(line):

    numbers = [char for char in line if char.isdigit()]

    if numbers:
        return int(numbers[0] + numbers[-1])
    return 0

def sum_of_calibration_values(file_path):

    with open(file_path, 'r') as file:
        lines = file.readlines()

    calibration_values = [find_calibration_value_from_line(line.strip()) for line in lines]

    total_sum = sum(calibration_values)

    return total_sum


file_path = '../TextFiles/day1.txt'
total_sum = sum_of_calibration_values(file_path)
print(f"The total sum of calibration values is: {total_sum}")
