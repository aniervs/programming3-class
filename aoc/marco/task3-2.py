import sys

ans = 0

grid = []
for line in sys.stdin:
    grid.append(line.strip())

n = len(grid)
m = len(grid[0])

is_part = [[False] * m for _ in range(n)]

def get_number(i, j):
    while j > 0 and grid[i][j - 1].isnumeric():
        j -= 1
    res = 0
    while j < m and grid[i][j].isnumeric():
        res *= 10
        res += int(grid[i][j])
        j += 1
    return res

for i in range(n):
    for j in range(m):
        if grid[i][j] != '*':
            continue
        numbers = []
        for dx in range(-1,2):
            for dy in range(-1,2):
                x = i + dx
                y = j + dy
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                if not grid[x][y].isnumeric():
                    continue
                if dy < 1 and grid[x][y+1].isnumeric():
                    continue
                numbers.append(get_number(x, y))
        if len(numbers) == 2:
            ans += numbers[0] * numbers[1]



print(ans)
