

import collections

def evaluate_hand(hand):
    ranks = "AKQJT98765432"
    rank_dict = {rank: i for i, rank in enumerate(ranks, start=1)}
    count = collections.Counter(hand)
    score, hand_ranks = zip(*sorted(((count[rank], rank_dict[rank]) for rank in count), reverse=True))

    if score == (5,):
        hand_type = 8  # Five of a kind
    elif score == (4, 1):
        hand_type = 7  # Four of a kind
    elif score == (3, 2):
        hand_type = 6  # Full house
    elif score == (3, 1, 1):
        hand_type = 5  # Three of a kind
    elif score == (2, 2, 1):
        hand_type = 4  # Two pair
    elif score == (2, 1, 1, 1):
        hand_type = 3  # One pair
    else:
        hand_type = 1  # High card

    return (hand_type,) + hand_ranks

def calculate_total_winnings(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    hands_with_bids = [(line.split()[0], int(line.split()[1])) for line in lines]
    evaluated_hands = sorted([(evaluate_hand(hand), bid) for hand, bid in hands_with_bids], reverse=True)

    total_winnings = sum(bid * (rank + 1) for rank, (_, bid) in enumerate(evaluated_hands))
    return total_winnings

# The file_path needs to be set to the actual path of the Exercise7.txt file
file_path = '../TextFiles/day7.txt'  # Update this to your actual file path
total_winnings = calculate_total_winnings(file_path)
print(f"Total winnings: {total_winnings}")
