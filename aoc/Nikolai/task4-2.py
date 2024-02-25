def part2(data):
    cards = [1] * len(data)

    for i in range(len(data)):
        w, my = data[i].split(":")[1].split("|")
        w = set(w.split())
        my = set(my.split())
        match = len(w & my)
        for j in range(1, match + 1):
            cards[i + j] += cards[i]

    return sum(cards)

file_path = "files/task4"
with open(file_path, 'r') as file:
    text = file.read()
arr = text.split('\n')
print(part2(arr))