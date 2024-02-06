def part2(data):
    cards = [1] * len(data)

    for i, line in enumerate(data):
        winning, yours = map(set, map(str.split, line.split(":")[1].split("|")))
        matched_count = len(winning & yours)
        for j in range(1, matched_count + 1):
            cards[i + j] += cards[i]
    return sum(cards)


with open('input2-1.txt', 'r') as file:
    lines = file.readlines()
    print(part2(lines))
