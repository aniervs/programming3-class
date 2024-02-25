with open('task11.txt', 'r') as file:
    text = file.read()

def calculate_manhattan_distance(data):
    nums = []
    matr_y = [0]
    matr_x = [0]


    for i in range(len(data)):
        is_clear_row = all(cell != '#' for cell in data[i])

        for j in range(len(data[i])):
            if data[i][j] == "#":
                nums.append((i, j))

        matr_y.append(matr_y[i])
        if is_clear_row:
            matr_y[i + 1] += 1

    for i in range(len(data[0])):
        is_clear_col = all(data[j][i] != '#' for j in range(len(data)))

        matr_x.append(matr_x[i])
        if is_clear_col:
            matr_x[i + 1] += 1

    total_sum = 0

    for i in range(len(nums)):
        for y, x in nums[i + 1:]:
            total_sum += abs(x - nums[i][1]) + abs(matr_x[x] - matr_x[nums[i][1]])
            total_sum += abs(y - nums[i][0]) + abs(matr_y[y] - matr_y[nums[i][0]])

    return total_sum



arr = text.split('\n')
print(calculate_manhattan_distance(arr))
