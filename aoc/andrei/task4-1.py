def part1(data):
    points = 0
    for line in data:
        w, my = line.split(":")[1].split("|")
        w = set(w.split())
        my = set(my.split())
        match = len(w & my)
        if match > 0:
            points += 2 ** (match - 1)
    return points

file_path = "files/task4"
with open(file_path, 'r') as file:
    text = file.read()
arr = text.split('\n')
print(part1(arr))