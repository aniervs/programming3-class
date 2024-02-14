class Galaxy:
    def __init__(self, row, col):
        self.row = row
        self.col = col

def get_dist(ga, gb, row_is_empty, col_is_empty):
    dr = abs(ga.row - gb.row)
    dc = abs(ga.col - gb.col)

    dist = dr + dc
    for i in range(min(ga.row, gb.row) + 1, max(ga.row, gb.row)):
        dist += (1_000_000 - 1) * row_is_empty[i]
    for j in range(min(ga.col, gb.col) + 1, max(ga.col, gb.col)):
        dist += (1_000_000 - 1) * col_is_empty[j]
    return dist

def find_galaxies():
    with open("./txt/day11.txt", "r") as file:
        grid = [line.strip() for line in file]

    row_is_empty = [True] * len(grid)
    col_is_empty = [True] * len(grid[0])

    galaxies = []

    # find galaxies
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
