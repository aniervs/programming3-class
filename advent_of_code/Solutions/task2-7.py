

def hand_strength(hand):
    # Order of card labels from highest to lowest
    order = 'AKQJT98765432'
    # Count the occurrences of each card label in the hand
    counts = {label: hand.count(label) for label in set(hand)}
    # Sort the counts by frequency and then by card label strength
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], -order.index(x[0])))

    # Identify the hand type based on the counts of each card label
    if sorted_counts[0][1] == 5:
        return (8, [order.index(sorted_counts[0][0])])  # Five of a kind
    if sorted_counts[0][1] == 4:
        return (7, [order.index(sorted_counts[0][0])])  # Four of a kind
    if sorted_counts[0][1] == 3 and sorted_counts[1][1] == 2:
        return (6, [order.index(sorted_counts[0][0]), order.index(sorted_counts[1][0])])  # Full house
    if sorted_counts[0][1] == 3:
        return (5, [order.index(sorted_counts[0][0])])  # Three of a kind
    if sorted_counts[0][1] == 2 and sorted_counts[1][1] == 2:
        return (4, [order.index(sorted_counts[0][0]), order.index(sorted_counts[1][0])])  # Two pair
    if sorted_counts[0][1] == 2:
        return (3, [order.index(sorted_counts[0][0])])  # One pair
    return (2, [order.index(label) for label in hand])  # High card


# Function to calculate total winnings
def calculate_total_winnings(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Parse hands and bids
    hands_and_bids = [line.split() for line in lines]
    hands = [hand for hand, bid in hands_and_bids]
    bids = [int(bid) for hand, bid in hands_and_bids]

    # Determine the strength of each hand
    strengths = [hand_strength(hand) for hand in hands]

    # Sort the hands by their strength (type and then by the strength within the type)
    sorted_indices = sorted(range(len(hands)), key=lambda i: strengths[i], reverse=True)

    # Calculate winnings
    total_winnings = sum(bids[i] * (rank + 1) for rank, i in enumerate(sorted_indices))

    return total_winnings


total_winnings = calculate_total_winnings('../TextFiles/day7.txt')
print(total_winnings)


