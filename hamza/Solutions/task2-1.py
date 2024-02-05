



# Define a function to extract the calibration value from a single line
def find_calibration_value_from_line(line):
    # Extract all digits from the line
    numbers = [char for char in line if char.isdigit()]
    # Combine the first and last digit to form a two-digit number
    if numbers:
        return int(numbers[0] + numbers[-1])
    return 0

# Define the function that processes a text file and finds the sum of calibration values
def sum_of_calibration_values(file_path):
    # Open the file and read the lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Calculate the calibration values for each line
    calibration_values = [find_calibration_value_from_line(line.strip()) for line in lines]
    # Calculate the total sum of calibration values
    total_sum = sum(calibration_values)

    return total_sum

# Example usage with a given file path
# Replace 'path_to_your_file.txt' with the actual path to your '.txt' file
file_path = '../TextFiles/day1.txt'
total_sum = sum_of_calibration_values(file_path)
print(f"The total sum of calibration values is: {total_sum}")
