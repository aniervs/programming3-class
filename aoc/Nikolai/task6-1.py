def part1(data):
    time = data[0].split(":")
    time = time[1].split(" ")
    records = data[1].split(":")
    records = records[1].split(" ")
    ans = 1
    j = 0
    for i in range(len(time)):
        while j < int(time[i]):
            if (int(time[i]) - j) * j > int(records[i]):

                break
            j+=1
        ans *= int(time[i]) - j * 2 + 1

    return ans

#in input file deleted spaces manualy
file_path = "files/task6"
with open(file_path, 'r') as file:
    text = file.read()
arr = text.split('\n')
print(part1(arr))