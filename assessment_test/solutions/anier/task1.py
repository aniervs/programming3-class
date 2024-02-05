def spiral(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    r, c = 0, 0
    dr, dc = 0, 1
    min_r, min_c = 0, 0
    max_r, max_c = n-1, m-1
    result = []
    
    for _ in range(n * m):
        result.append(matrix[r][c])
        r += dr
        c += dc
        if r < min_r:
            r = min_r
            c += 1
            dr, dc = 0, 1
            min_c += 1
        elif r > max_r:
            r = max_r
            c -= 1
            dr, dc = 0, -1
            max_c -= 1
        elif c < min_c:
            c = min_c
            r -= 1
            dr, dc = -1, 0
            max_r -= 1
        elif c > max_c:
            c = max_c
            r += 1
            dr, dc = 1, 0
            min_r += 1
        
    
    return result

assert spiral([[1,2,3],
               [4,5,6],
               [7,8,9]]) == [1,2,3,6,9,8,7,4,5]

assert spiral([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

assert spiral([[1, 2],[3, 4],[5, 6]]) == [1, 2, 4, 6, 5, 3]
