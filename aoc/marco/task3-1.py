import sys

ans = 0

grid = []
for line in sys.stdin:
    grid.append(line.strip())

n = len(grid)
m = len(grid[0])

is_part = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == '.' or grid[i][j].isnumeric():
            continue
        for dx in range(-1,2):
            for dy in range(-1,2):
                x = i + dx
                y = j + dy
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                is_part[x][y] = True

for i in range(n):
    sum = 0
    legal = False
    for j in range(m):
        if grid[i][j].isnumeric():
            sum *= 10
            sum += int(grid[i][j])
            if is_part[i][j]:
                legal = True
        else:
            if legal:
                ans += sum
                legal = False
            sum = 0
    if legal:
        ans += sum

print(ans)
