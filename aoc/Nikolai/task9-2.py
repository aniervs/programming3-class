
def part2(data):
    ans = 0
    for i in range(len(data)):
        arr = data[i].split(" ")[::-1]
        matr = [[0 for _ in range(len(arr) - _ + 1)] for _ in range(len(arr))]
        matr[0] = arr + [0]
        j = 0
        while j < (len(arr) - 1):
            flag = True
            for k in range(1, len(arr) - j):
                if matr[j][k] != 0:
                    flag = False
                matr[j + 1][k - 1] = int(matr[j][k]) - int(matr[j][k - 1])
            if flag:
                break
            j += 1
        while j >= 0:
            matr[j][len(arr) - j] = int(matr[j][len(arr) - j - 1]) +int(matr[j + 1][len(arr) - j - 1])
            j -=1
        ans += matr[0][len(arr)]
    return ans


file_path = "files/task9"
with open(file_path, 'r') as file:
    text = file.read()
arr = text.split('\n')
print(part2(arr))