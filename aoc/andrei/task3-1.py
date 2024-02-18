file_path = "files/task3"
with open(file_path, 'r') as file:
    text = file.read()
data = [list(cur) for cur in text.split('\n')]

n = len(data)
m = len(data[0])

adj = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

nums = []

ans = 0

for i in range(n):
    for j in range(m):
        if not data[i][j].isdigit() and data[i][j] != '.':
            for step in adj:
                if i+step[0] < n and i+step[0] >= 0 and j+step[1] < m and j+step[1] >= 0 and data[i+step[0]][j+step[1]].isdigit():
                    nums.append((i+step[0], j+step[1]))

for cur in nums:
    starti = cur[0]
    startj = cur[1]
    if data[starti][startj] == '.':
        continue

    curj = startj-1
    curnum = data[starti][startj]
    data[starti][startj] = '.'
    while curj >= 0 and data[starti][curj].isdigit():
        curnum = data[starti][curj] + curnum
        data[starti][curj] = '.'
        curj -= 1


    curj = startj+1
    while curj < m and data[starti][curj].isdigit():
        curnum += data[starti][curj]
        data[starti][curj] = '.'
        curj += 1

    ans += int(curnum)

print(ans)