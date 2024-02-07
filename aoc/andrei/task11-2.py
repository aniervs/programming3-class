def part1(data):
    nums = []
    matr_y = [0]
    matr_x = [0]
    for i in range(len(data)):
        is_clear = True
        for j in range(len(data[i])):
            if data[i][j] == "#":
                is_clear = False
                nums.append((i,j))
        matr_y.append(matr_y[i])
        if(is_clear):
            matr_y[i+1] += 1000000 - 1


    for i in range(len(data[0])):
        is_clear = True
        for j in range(len(data)):
            if data[j][i] == "#":
                is_clear = False
        matr_x.append(matr_x[i])
        if(is_clear):
            matr_x[i+1] += 1000000 - 1

    sum = 0

    for i in range(len(nums)):

        for y, x in nums[i+1:]:
            sum += abs(x - nums[i][1]) + abs(matr_x[x] - matr_x[nums[i][1]])
            sum += abs(y - nums[i][0]) + abs(matr_y[y] - matr_y[nums[i][0]])


    return sum






file_path = "files/task11"
with open(file_path, 'r') as file:
    text = file.read()
arr = text.split('\n')
print(part1(arr))