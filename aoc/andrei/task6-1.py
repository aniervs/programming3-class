def part1(data):
    time = data[0].split(":")
    time = time[1].split(" ")
    time = list(filter(lambda a: a != '', time))
    records = data[1].split(":")
    records = records[1].split(" ")
    records = list(filter(lambda a: a != '', records))
    ans = 1
    j = 0
    for i in range(len(time)):
        j = 0
        while j < int(time[i]):
            if (int(time[i]) - j) * j > int(records[i]):
                break
            j+=1
        ans *= int(time[i]) - j * 2 + 1


    return ans


file_path = "files/task6"
with open(file_path, 'r') as file:
    text = file.read()
arr = text.split('\n')
print(part1(arr))