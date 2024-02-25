from functools import reduce

def calculate_product_of_adjacent_numbers(data):
    matrix = [['.' for _ in range(len(data[0]))] for _ in range(len(data))]

    for i in range(len(data)):
        j = 0
        while j < len(data[i]):
            if j < len(data[i]) and data[i][j].isdigit():
                length = 1
                while j + length < len(data[i]) and data[i][j + length].isdigit():
                    length += 1
                num = data[i][j:j + length]

                while length > 0:
                    matrix[i][j] = num
                    length -= 1
                    j += 1
            else:
                matrix[i][j] = data[i][j]
                j += 1

    result = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "*":
                unique_numbers = set()
                for row in range(i - 1, i + 2):
                    for col in range(j - 1, j + 2):
                        if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
                            if matrix[row][col].isdigit():
                                unique_numbers.add(int(matrix[row][col]))

                if len(unique_numbers) > 1:
                    result += reduce(lambda x, y: x * y, unique_numbers)

    return result

with open('task3.txt', 'r') as file:
    content = file.read()

lines = content.split('\n')
print(calculate_product_of_adjacent_numbers(lines))
