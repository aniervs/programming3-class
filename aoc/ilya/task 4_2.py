def calculate_winning_ways(data):
    cards = [1] * len(data)

    for i, line in enumerate(data):
        winning, yours = map(set, map(str.split, line.split(":")[1].split("|")))
        matched_count = len(winning & yours)

        for j in range(1, matched_count + 1):
            cards[i + j] += cards[i]

    return sum(cards)

with open('task4.txt', 'r') as file:
    lines = file.readlines()
    print(calculate_winning_ways(lines))
