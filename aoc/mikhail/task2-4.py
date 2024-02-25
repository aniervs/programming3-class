def calculate_card_points_from_file(file_path):
    """
    Calculate the total points for all scratchcards from the file.
    """
    def calculate_points(card_line):
        parts = card_line.split('|')
        winning_numbers = set(map(int, parts[0].split()[2:]))  
        your_numbers = set(map(int, parts[1].split()))

        matches = winning_numbers.intersection(your_numbers)
        if not matches:
            return 0

        return 2 ** (len(matches) - 1)

    total = 0
    with open(file_path, 'r') as file:
        for card in file:
            total += calculate_points(card.strip())

    return total

file_path = 'aoc/mikhail/puzzles_input/puzzle4.txt'

total_scratchcard_points = calculate_card_points_from_file(file_path)
total_scratchcard_points

print(total_scratchcard_points)
