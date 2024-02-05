


def read_file_and_sum_part_numbers(file_path):
    # Read the file content
    with open(file_path, 'r') as file:
        file_content = file.readlines()
        file_content = [line.strip() for line in file_content]

    symbols = set("*#$+")
    sum_parts = 0

    # Check if a position is adjacent to a symbol
    def is_adjacent_to_symbol(x, y, grid):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] in symbols:
                return True
        return False

    for i, row in enumerate(file_content):
        j = 0
        while j < len(row):
            if row[j].isdigit():
                number = row[j]
                k = j + 1
                while k < len(row) and row[k].isdigit():
                    number += row[k]
                    k += 1
                # Check if either the start or the end of the number is adjacent to a symbol
                if is_adjacent_to_symbol(i, j, file_content) or is_adjacent_to_symbol(i, k-1, file_content):
                    sum_parts += int(number)
                j = k
            else:
                j += 1

    return sum_parts

# Assuming the file 'hey.txt' is located in the 'TextFiles' directory
file_path = '../TextFiles/day3.txt'  # Update this path if necessary

# Calculate the sum of part numbers
sum_parts = read_file_and_sum_part_numbers(file_path)

print(f"The sum of part numbers in the file is: {sum_parts}")