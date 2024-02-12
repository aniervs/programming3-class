from collections import Counter
from functools import cmp_to_key

with open('./txt/day7.txt', 'r') as file:
    hands = [line.strip().split() for line in file]

def hand_strength(hand):
    card_counts = Counter(hand)
    unique_counts = Counter(card_counts.values())
    most_common_count = max(unique_counts)

    if most_common_count >= 4:
        return most_common_count + 2
    elif most_common_count == 3:
        return 4 + int(2 in unique_counts)
    elif most_common_count == 2:
        return 2 + int(unique_counts[2] == 2)
    else:
        return 1

def compare_hands(hand1, hand2):
    strength1 = hand_strength(hand1[0])
    strength2 = hand_strength(hand2[0])

    if strength1 == strength2:
        tie_rank_order = 'AKQJT98765432'
        for card1, card2 in zip(hand1[0], hand2[0]):
            tie_rank1 = tie_rank_order.index(card1)
            tie_rank2 = tie_rank_order.index(card2)
            if tie_rank1 != tie_rank2:
                return tie_rank2 - tie_rank1
    else:
        return strength1 - strength2

hands.sort(key=cmp_to_key(compare_hands))

total_score = 0

for rank, (hand, bid) in enumerate(hands, 1):
    hand_score = rank * int(bid)
    total_score += hand_score
    print(f"Hand: {hand}, Rank: {rank}, Bid: {bid}, Hand Score: {hand_score}")

print("Total Score:", total_score)
