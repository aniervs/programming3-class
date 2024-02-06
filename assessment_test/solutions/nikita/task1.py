def spiral(matrix):
    result = []
    dir = 'right'
    row, col = 0, 0
    right = len(matrix[0])
    left = 0
    top = 0
    bottom = len(matrix)

    for _ in range(right*bottom):
        result.append(matrix[row][col])
        if dir == 'right':
            col += 1
            if col == right-1:
                dir = 'down'
                right -= 1
        elif dir == 'left':
            col -= 1
            if col == left:
                dir = 'up'
                left += 1
        elif dir == 'down':
            row += 1
            if row == bottom-1:
                dir = 'left'
                bottom -= 1
        else:
            row -= 1
            if row == top+1:
                dir = 'right'
                top += 1

    return result


matrix = [
    [1, 2, 4, 10],
    [7, 6, 5, 12],
    [11, 15, 16, 17],
    [8, 3, 9, 19]
]
print(spiral(matrix))
