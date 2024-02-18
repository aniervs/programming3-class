def part1(data):
    matrix = [['.' for _ in range(len(data[0]))] for _ in range(len(data))]
    for i in range(len(data)):
        j = 0
        while j < len(data[i]):
            if j < len(data[i]) and data[i][j].isdigit():
                l = 1
                while j+l < len(data[i]) and data[i][j+l].isdigit():
                    l += 1
                num = data[i][j:j+l]

                while l > 0:
                    matrix[i][j] = num
                    l-=1
                    j+=1
            else:
                matrix[i][j] = data[i][j]
                j+=1
        a = set([])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not matrix[i][j].isdigit() and matrix[i][j] != ".":
                for row in range(i - 1, i + 2):
                    for col in range(j - 1, j + 2):
                        if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
                            if matrix[row][col].isdigit():
                                a.add(int(matrix[row][col]))
    return sum(a)

file_path = "files/task3"
with open(file_path, 'r') as file:
    text = file.read()
arr = text.split('\n')
print(part1(arr))