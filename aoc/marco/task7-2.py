import sys

sum = 0

cards = []

def get_type(card):
    cnt = {}
    jokers = 0
    for c in card:
        if c == "J":
            jokers += 1
            continue
        if not c in cnt:
            cnt[c] = 0
        cnt[c] += 1
    if len(cnt) == 0:
        return 0 # five of a kind
    if max(cnt.values()) + jokers == 5:
        return 0 # five of a kind
    if max(cnt.values()) + jokers == 4:
        return 1 # four of a kind
    if len(cnt) <= 2:
        return 2 # full house
    if max(cnt.values()) + jokers == 3:
        return 3 # three of a kind
    if jokers == 0:
        if max(cnt.values()) == 2 and len(cnt) == 3:
            return 4 # two pair
    if jokers == 1:
        if max(cnt.values()) == 2:
            return 4 # two pair
    if max(cnt.values()) + jokers == 2:
        return 5 # one pair
    return 6

def card_strength(card):
    if card == 'A':
        return 0
    if card == 'K':
        return 1
    if card == 'Q':
        return 2
    if card == 'T':
        return 4
    if card == '9':
        return 5
    if card == '8':
        return 6
    if card == '7':
        return 7
    if card == '6':
        return 8
    if card == '5':
        return 9
    if card == '4':
        return 10
    if card == '3':
        return 11
    if card == '2':
        return 12
    if card == 'J':
        return 13

def map_key(card):
    return [get_type(card[0]), list(map(card_strength, card[0]))]

for line in sys.stdin:
    card, price = line.strip().split(" ")
    cards.append([card, int(price)])


cards.sort(key=map_key)
cards = cards[::-1]
for i in range(len(cards)):
    sum += (i + 1) * cards[i][1]

print(cards)
print(sum)

