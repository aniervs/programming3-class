def getSpiral(matrix):
    n = len(matrix)
    m = len(matrix[0])
    x = 0
    y = 0
    ans = []
    walkx = n-1
    walky = m-1
    dir = 1
    for i in range(m):
        ans.append(matrix[x][y])
        y += 1
    y -= 1
    while walkx > 0 and walky > 0:
        for i in range(walkx):
            x += dir
            ans.append(matrix[x][y])

        for i in range(walky):
            y -= dir
            ans.append(matrix[x][y])
        dir *= -1
        walkx -= 1
        walky -= 1

    return ans

m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

m2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print(getSpiral(m1))
print(getSpiral(m2))