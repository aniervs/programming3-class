
# Define the path to the file
file_path = '../TextFiles/day4.txt'

# Function to read the file and calculate points
def calculate_points(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    total_points = 0
    for line in lines:
        parts = line.strip().split('|')
        if len(parts) != 2:
            continue  # Skip lines that don't have the expected format

        # Split the winning numbers and the numbers you have
        winning_numbers = set(map(int, parts[0].split(':')[1].strip().split()))
        numbers_you_have = set(map(int, parts[1].strip().split()))

        # Calculate matches
        matches = winning_numbers.intersection(numbers_you_have)
        if matches:
            # Calculate points for this card
            points = 1  # Start with one point for the first match
            for _ in range(1, len(matches)):  # Double for each additional match
                points *= 2
            total_points += points

    return total_points

# Calculate the points
total_points = calculate_points(file_path)
print(total_points)


