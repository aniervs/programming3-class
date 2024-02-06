import sys

def read_list(l):
    return [int(x) for x in l.split(" ") if x != ""]

cards = []
for line in sys.stdin:
    cards.append(line.strip().split(": ")[1])

count = [1] * len(cards)

for i in range(len(cards)):
    card = cards[i]
    winning, yours = list(map(read_list, card.split(" | ")))
    winning = set(winning)
    points = 0
    for x in yours:
        if x in winning:
            points += 1
    for j in range(points):
        count[i + j + 1] += count[i]

print(sum(count))
