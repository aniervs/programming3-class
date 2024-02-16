import sys

class Galaxy:
    def __init__(self, row, col):
        self.row = row
        self.col = col

def get_dist(ga, gb, row_is_empty, col_is_empty):
    dr = abs(ga.row - gb.row)
    dc = abs(ga.col - gb.col)

    dist = dr + dc
    for i in range(min(ga.row, gb.row) + 1, max(ga.row, gb.row)):
        dist += row_is_empty[i]
    for j in range(min(ga.col, gb.col) + 1, max(ga.col, gb.col)):
        dist += col_is_empty[j]
    return dist

with open("./txt/day11.txt", "r") as file:
    grid = [line.strip() for line in file]

def find_galaxies():
    row_is_empty = [True] * len(grid)
    col_is_empty = [True] * len(grid[0])

    galaxies = []


    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                row_is_empty[i] = False
                col_is_empty[j] = False

                galaxy = Galaxy(i, j)
                galaxies.append(galaxy)

    ans = 0
    for a_idx in range(len(galaxies)):
        for b_idx in range(a_idx + 1, len(galaxies)):
            ga = galaxies[a_idx]
            gb = galaxies[b_idx]

            dist = get_dist(ga, gb, row_is_empty, col_is_empty)

            ans += dist

    print("res", ans)


find_galaxies()