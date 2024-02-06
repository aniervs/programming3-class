import sys

ans = 0
grid = []

for line in sys.stdin:
    grid.append(line.strip())

# duplicate rows
i = 0
while i < len(grid):
    cnt = 0
    for j in range(len(grid[0])):
        if grid[i][j] == '#':
            cnt += 1
    if cnt == 0:
        # duplicate row i
        grid = [*grid[:i], "." * len(grid[i]), *grid[i:]]
        i += 2
    else:
        i += 1

# duplicate columns
i = 0
while i < len(grid[0]):
    cnt = 0
    for j in range(len(grid)):
        if grid[j][i] == '#':
            cnt += 1
    if cnt == 0:
        # duplicate column i
        for j in range(len(grid)):
            grid[j] = grid[j][:i] + "." + grid[j][i:]
        i += 2
    else:
        i += 1

n = len(grid)
m = len(grid[0])

# sum up x difference
cnt = 0
sm = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "#":
            ans += cnt * i
            ans -= sm
    for j in range(m):
        if grid[i][j] == "#":
            cnt += 1
            sm += i

# sum up y difference
cnt = 0
sm = 0
for j in range(m):
    for i in range(n):
        if grid[i][j] == "#":
            ans += cnt * j
            ans -= sm
    for i in range(n):
        if grid[i][j] == "#":
            cnt += 1
            sm += j

print(ans)
