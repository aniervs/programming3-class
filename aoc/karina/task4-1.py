def part1(data):
    points = 0
    for line in data:
        winning, yours = map(set, map(str.split, line.split(":")[1].split("|")))
        points += int(2 ** (len(winning & yours) - 1))
    return points


with open('input2-1.txt', 'r') as file:
    lines = file.readlines()
    print(part1(lines))
