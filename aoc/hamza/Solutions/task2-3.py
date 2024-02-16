
def sum_part_numbers(schematic):
    # 2D list (grid) of characters
    lines = schematic.strip().split("\n")
    grid = [list(line) for line in lines]

    # 8 possible movements (horizontal, vertical, and diagonal)
    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def has_adjacent_symbol(x, y):
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if not grid[nx][ny].isdigit() and grid[nx][ny] != '.':
                    return True
        return False

    sum_parts = 0
    number_buffer = ""
    adjacent_to_symbol = False

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y].isdigit():
                number_buffer += grid[x][y]
                adjacent_to_symbol = adjacent_to_symbol or has_adjacent_symbol(x, y)
            else:
                if number_buffer and adjacent_to_symbol:
                    sum_parts += int(number_buffer)
                number_buffer = ""
                adjacent_to_symbol = False
        if number_buffer and adjacent_to_symbol:
            sum_parts += int(number_buffer)
        number_buffer = ""
        adjacent_to_symbol = False

    return sum_parts

def read_schematic_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

file_path = '../TextFiles/day3.txt'
schematic = read_schematic_from_file(file_path)
sum_of_part_numbers = sum_part_numbers(schematic)
print(sum_of_part_numbers)

