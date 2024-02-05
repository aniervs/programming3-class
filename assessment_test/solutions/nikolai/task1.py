def spiral(arr):
    top = 0
    bottom = len(arr[0]) - 1
    left = 0
    right = len(arr) - 1
    w = 0
    while (top <= bottom and left <= right):
        if w == 0:
            for i in range(left, right + 1):
                print(str(arr[top][i]) + " ")
            top += 1

        elif w == 1:
            for i in range(top, bottom + 1):
                print(str(arr[i][right]) + " ")

            right -= 1

        elif w == 2:
            for i in range(right, left - 1, -1):
                print(str(arr[bottom][i]) + " ")

            bottom -= 1

        elif w == 3:
            for i in range(bottom, top - 1, -1):
                print(str(arr[i][left]) + " ")
            left += 1

        w += 1
        w %= 4

array = [[1, 2, 3, 4],
         [12, 13, 14, 5],
         [11, 16, 15, 6],
         [10, 9, 8, 7]]

spiral(array)