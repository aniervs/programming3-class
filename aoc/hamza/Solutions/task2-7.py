

def hand_strength(hand):

    order = 'AKQJT98765432'

    counts = {label: hand.count(label) for label in set(hand)}

    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], -order.index(x[0])))

    if sorted_counts[0][1] == 5:
        return (8, [order.index(sorted_counts[0][0])])
    if sorted_counts[0][1] == 4:
        return (7, [order.index(sorted_counts[0][0])])
    if sorted_counts[0][1] == 3 and sorted_counts[1][1] == 2:
        return (6, [order.index(sorted_counts[0][0]), order.index(sorted_counts[1][0])])
    if sorted_counts[0][1] == 3:
        return (5, [order.index(sorted_counts[0][0])])
    if sorted_counts[0][1] == 2 and sorted_counts[1][1] == 2:
        return (4, [order.index(sorted_counts[0][0]), order.index(sorted_counts[1][0])])
    if sorted_counts[0][1] == 2:
        return (3, [order.index(sorted_counts[0][0])])
    return (2, [order.index(label) for label in hand])


def calculate_total_winnings(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    hands_and_bids = [line.split() for line in lines]
    hands = [hand for hand, bid in hands_and_bids]
    bids = [int(bid) for hand, bid in hands_and_bids]

    strengths = [hand_strength(hand) for hand in hands]

    sorted_indices = sorted(range(len(hands)), key=lambda i: strengths[i], reverse=True)

    total_winnings = sum(bids[i] * (rank + 1) for rank, i in enumerate(sorted_indices))

    return total_winnings


total_winnings = calculate_total_winnings('../TextFiles/day7.txt')
print(total_winnings)


