from functools import cmp_to_key
card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

def compare_hands(hand1, hand2):
    for card1, card2 in zip(hand1[0], hand2[0]):
        if card_values[card1[0]] != card_values[card2[0]]:
            return card_values[card2[0]] - card_values[card1[0]]
    return 0
def part3(data):
    scoring = [[] for i in range(7)]
    for i in range(len(data)):
        amount = {"A":0, "K":0, "Q":0, "J":0, "T":0, "9":0, "8":0, "7":0, "6":0, "5":0,"4":0, "3":0, "2":0}
        cards, score = data[i].split(" ")
        mx = 0
        secpair = False
        for j in range(len(cards)):
            amount[cards[j]] += 1
            if amount[cards[j]] > mx:
                mx = amount[cards[j]]
        if mx == 2 or mx == 3:
            for val in amount.values():
                if val == 2:
                    secpair = True
        if mx == 5:
            scoring[0].append([cards, score])
        elif mx == 4:
            scoring[1].append([cards, score])
        elif mx == 3 and secpair:
            scoring[2].append([cards, score])
        elif mx == 3:
            scoring[3].append([cards, score])
        elif mx == 2 and secpair:
            scoring[4].append([cards, score])
        elif mx == 2:
            scoring[5].append([cards, score])
        else:
            scoring[6].append([cards, score])

    ans = 0
    it = 0
    for i in range(len(scoring)):
        scoring[i] = sorted(scoring[i], key=cmp_to_key(compare_hands))
        for j in range(len(scoring[i])):
            ans += (len(data) - it) * int(scoring[i][j][1])
            print(int(scoring[i][j][1]), len(data) - it)
            it += 1
    return ans


file_path = "files/task7"
with open(file_path, 'r') as file:
    text = file.read()
arr = text.split('\n')


def part1(data):
    hands = [line.split() for line in data]
    print(hands)
    hands = [(label_to_number(hand[0]), int(hand[1]), get_score(hand[0])) for hand in hands]
    hands = sorted(hands, key=lambda hand: (hand[2], hand[0]))
    return sum(rank * hand[1] for rank, hand in enumerate(hands, 1))


def part2(data):
    hands = [line.split() for line in data]
    hands = [(label_to_number(hand[0], wildcard=True), int(hand[1]), get_score(hand[0], wildcard=True))
             for hand in hands]
    hands = sorted(hands, key=lambda hand: (hand[2], hand[0]))
    return sum(rank * hand[1] for rank, hand in enumerate(hands, 1))


def label_to_number(cards, wildcard=False):
    mapping = {
        "T": 10,
        "J": 1 if wildcard else 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    return [int(mapping.get(i, i)) for i in cards]


def get_score(cards, wildcard=False):
    types = {
        50: "Five of a kind",
        40: "Four of a kind",
        32: "Full house",
        30: "Three of a kind",
        22: "Two pair",
        20: "One pair",
        10: "High card",
    }
    counter = {}
    cards = list(cards)

    jokers = 0
    if wildcard:
        jokers = cards.count("J")
        cards = [i for i in cards if i != "J"]

    for card in cards:
        counter[card] = cards.count(card)

    _max, _2nd = (sorted(counter.values(), reverse=True) + [0] * 5)[:2]
    rank_score = 10 * (_max + jokers) + _2nd
    rank_score = max(i for i in types.keys() if i <= rank_score)

    # using rank_score as the part of the key to sort the hands
    # and types[rank_score] for the debug purpose
    return rank_score, types[rank_score]


print(part1(arr))