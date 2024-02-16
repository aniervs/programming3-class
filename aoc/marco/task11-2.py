import sys

ans = 0
grid = []
xpos = []
ypos = []

for line in sys.stdin:
    grid.append(line.strip())

n = len(grid)
m = len(grid[0])

# duplicate rows
i = 0
x = 0
while i < len(grid):
    cnt = 0
    for j in range(len(grid[0])):
        if grid[i][j] == '#':
            cnt += 1
    if cnt == 0:
        x += 1000000
    else:
        x += 1
    xpos.append(x)
    i += 1

# duplicate columns
i = 0
y = 0
while i < len(grid[0]):
    cnt = 0
    for j in range(len(grid)):
        if grid[j][i] == '#':
            cnt += 1
    if cnt == 0:
        y += 1000000
    else:
        y += 1
    ypos.append(y)
    i += 1

# sum up x difference
cnt = 0
sm = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "#":
            ans += cnt * xpos[i]
            ans -= sm
    for j in range(m):
        if grid[i][j] == "#":
            cnt += 1
            sm += xpos[i]

# sum up y difference
cnt = 0
sm = 0
for j in range(m):
    for i in range(n):
        if grid[i][j] == "#":
            ans += cnt * ypos[j]
            ans -= sm
    for i in range(n):
        if grid[i][j] == "#":
            cnt += 1
            sm += ypos[j]

print(ans)
