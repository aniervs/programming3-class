# sk = [
#     ['4', '6', '7', '.', '.', '1', '1', '4', '.', '.'],
#     ['.', '.', '.', '*', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '3', '5', '.', '.', '6', '3', '3', '.'],
#     ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
#     ['6', '1', '7', '*', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '+', '.', '5', '8', '.'],
#     ['.', '.', '5', '9', '2', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '7', '5', '5', '.'],
#     ['.', '.', '.', '$', '.', '*', '.', '.', '.', '.'],
#     ['.', '6', '6', '4', '.', '5', '9', '8', '.', '.']
# ]

f = open('texts/task3', 'r')
sk = []
line = f.readline()[:-1]
while line != '':
    sp = []
    for symbol in line:
        sp.append(symbol)
    line = f.readline()[:-1]
    sk.append(sp)

def find_full_digit(sk, row, col):
    n = sk[row][col]
    orig_col = col
    if col + 1 < len(sk[0]) - 1:
        while sk[row][col+1].isdigit():
            n += sk[row][col+1]
            if col + 1 < len(sk[0]) - 1:
                col += 1
            else:
                break
    if orig_col-1 <= 0:
        while sk[row][orig_col-1].isdigit():
            n = sk[row][orig_col-1] + n
            if orig_col - 1 <= 0:
                orig_col -= 1
            else:
                break
    return n
S = set()
for row in range(len(sk)):
    for col in range(len(sk[row])):
        if not(sk[row][col].isdigit()) and sk[row][col] != '.':
            direction_y = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            direction_x = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            if row == 0:
                direction_y = directions[3:]
            elif row == len(sk)-1:
                direction_y = directions[:5]
            if col == 0:
                direction_x = directions[1:3] + directions[4] + directions[6:]
            elif col == len(sk[row])-1:
                direction_x = directions[:2] + directions[3] + directions[5:7]
            directions = [k for k in direction_y if k in direction_x]
            for x, y in directions:
                if sk[row + x][col + y].isdigit():
                    S.add(find_full_digit(sk, row+x, col+y))
print(S)
sum = 0
for i in S:
    sum += int(i)
print(sum)