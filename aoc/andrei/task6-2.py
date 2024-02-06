def part2(data):
    time = data[0].split(":")
    time = time[1].replace(' ','')
    records = data[1].split(":")
    records = records[1].replace(' ','')
    
    j = 0
    while j < int(time):
        if (int(time) - j) * j > int(records):
            break
        j+=1


    return int(time) - j * 2 + 1


file_path = "files/task6"
with open(file_path, 'r') as file:
    text = file.read()
arr = text.split('\n')
print(part2(arr))