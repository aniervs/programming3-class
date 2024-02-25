def spiral(a):
    top = 0
    bottom = len(a[0]) - 1
    left = 0
    right = len(a) - 1
    x = 0
    while (top <= bottom and left <= right):
        if x == 0:
            for i in range(left, right + 1):
                print(str(a[top][i]) + " ")
            top += 1

        elif x == 1:
            for i in range(top, bottom + 1):
                print(str(a[i][right]) + " ")

            right -= 1

        elif x == 2:
            for i in range(right, left - 1, -1):
                print(str(a[bottom][i]) + " ")

            bottom -= 1

        elif x == 3:
            for i in range(bottom, top - 1, -1):
                print(str(a[i][left]) + " ")
            left += 1

        x += 1
        x %= 4

arr = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]

spiral(arr)