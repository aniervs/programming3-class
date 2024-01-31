import unittest

def spiral_matrix(matrix):
    n = len(matrix[0])
    m = len(matrix)
    
    res = []
    left = 0
    right = n-1
    up = 0
    down = m-1
    d = 0
    while left <= right and up <= down:
        if d == 0:
            # remove top row
            for i in range(left,right+1):
                res.append(matrix[up][i])
            up += 1
        elif d == 1:
            # remove right column
            for i in range(up,down+1):
                res.append(matrix[i][right])
            right -= 1
        elif d == 2:
            # remove bottom row
            for i in range(right,left-1,-1):
                res.append(matrix[down][i])
            down -= 1
        else:
            # remove left column
            for i in range(down,up-1,-1):
                res.append(matrix[i][left])
            left += 1
        d = (d+1) % 4
    return res

class TestSpiralMatrix(unittest.TestCase):
    def test_square(self):
        res = spiral_matrix([
            [ 1,  2,  3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10,  9,  8, 7],
        ])
        self.assertEqual(res, list(range(1,17)))

    def test_rectangle(self):
        res1 = spiral_matrix([
            [ 1,  2, 3],
            [12, 13, 4],
            [11, 14, 5],
            [10, 15, 6],
            [ 9,  8, 7],
        ])
        self.assertEqual(res1, list(range(1,16)))

        res2 = spiral_matrix([
            [  1,  2,  3,  4, 5],
            [ 12, 13, 14, 15, 6],
            [ 11, 10,  9,  8, 7],
        ])
        self.assertEqual(res2, list(range(1,16)))

if __name__ == '__main__':
    unittest.main()
