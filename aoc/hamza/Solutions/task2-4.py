
file_path = '../TextFiles/day4.txt'

def calculate_points(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    total_points = 0
    for line in lines:
        parts = line.strip().split('|')
        if len(parts) != 2:
            continue

        winning_numbers = set(map(int, parts[0].split(':')[1].strip().split()))
        numbers_you_have = set(map(int, parts[1].strip().split()))

        matches = winning_numbers.intersection(numbers_you_have)
        if matches:

            points = 1
            for _ in range(1, len(matches)):
                points *= 2
            total_points += points

    return total_points

total_points = calculate_points(file_path)
print(total_points)


