from itertools import combinations

def expand_universe(input_lines):
    """
    Expand the universe by doubling rows and columns that contain no galaxies.
    """
    universe = [list(line.strip()) for line in input_lines]

    empty_rows = [i for i, row in enumerate(universe) if '#' not in row]
    empty_cols = [j for j in range(len(universe[0])) if all(universe[i][j] == '.' for i in range(len(universe)))]

    for i in sorted(empty_rows, reverse=True):
        universe.insert(i, universe[i])

    for j in sorted(empty_cols, reverse=True):
        for row in universe:
            row.insert(j, row[j])

    return universe

def find_galaxies(universe):
    """
    Find the positions of all galaxies in the universe.
    """
    galaxies = {}
    for i, row in enumerate(universe):
        for j, cell in enumerate(row):
            if cell == '#':
                galaxies[len(galaxies) + 1] = (i, j)
    return galaxies

def calculate_shortest_path_sum(universe, galaxies):
    """
    Calculate the sum of the shortest paths between all pairs of galaxies.
    """
    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    total_distance = 0
    for g1, g2 in combinations(galaxies.values(), 2):
        total_distance += manhattan_distance(g1, g2)

    return total_distance

def calculate_total_shortest_path_sum(file_path):
    """
    Calculate the total sum of the shortest path lengths between every pair of galaxies from the file.
    """
    with open(file_path, 'r') as file:
        puzzle_input = file.readlines()

    expanded_universe = expand_universe(puzzle_input)

    galaxies = find_galaxies(expanded_universe)

    total_sum = calculate_shortest_path_sum(expanded_universe, galaxies)

    return total_sum

file_path = 'aoc/mikhail/puzzles_input/puzzle11.txt'

sum_of_shortest_paths_day = calculate_total_shortest_path_sum(file_path)
sum_of_shortest_paths_day

print(sum_of_shortest_paths_day)
