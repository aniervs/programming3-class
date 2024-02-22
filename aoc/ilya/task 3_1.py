with open('task3.txt', 'r') as file:
    content = file.read()

grid = [list(row) for row in content.split('\n')]

rows = len(grid)
columns = len(grid[0])

directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

numbers = []
total_sum = 0

for i in range(rows):
    for j in range(columns):
        if not grid[i][j].isdigit() and grid[i][j] != '.':
            for step in directions:
                new_i, new_j = i + step[0], j + step[1]
                if 0 <= new_i < rows and 0 <= new_j < columns and grid[new_i][new_j].isdigit():
                    numbers.append((new_i, new_j))

for current_position in numbers:
    start_row, start_column = current_position
    if grid[start_row][start_column] == '.':
        continue

    current_column = start_column - 1
    current_number = grid[start_row][start_column]
    grid[start_row][start_column] = '.'

    while current_column >= 0 and grid[start_row][current_column].isdigit():
        current_number = grid[start_row][current_column] + current_number
        grid[start_row][current_column] = '.'
        current_column -= 1

    current_column = start_column + 1
    while current_column < columns and grid[start_row][current_column].isdigit():
        current_number += grid[start_row][current_column]
        grid[start_row][current_column] = '.'
        current_column += 1

    total_sum += int(current_number)

print(total_sum)
